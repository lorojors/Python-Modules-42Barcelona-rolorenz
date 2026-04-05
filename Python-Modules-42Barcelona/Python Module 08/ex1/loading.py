from __future__ import annotations

import importlib
import sys


# ---------------------------------------------------------------------------
# Dependency management
# ---------------------------------------------------------------------------

REQUIRED_PACKAGES: dict[str, str] = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
    "matplotlib": "Visualization",
}

OPTIONAL_PACKAGES: dict[str, str] = {
    "requests": "Network access",
}


def check_package(name: str) -> tuple[bool, str]:
    """Return (available, version_string)."""
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown")
        return True, version
    except ImportError:
        return False, ""


def check_dependencies() -> tuple[bool, dict[str, tuple[bool, str]]]:
    """Check all required and optional packages. Returns (all_required_ok, status_map)."""
    print("Checking dependencies:")
    status: dict[str, tuple[bool, str]] = {}
    all_ok = True

    for pkg, desc in {**REQUIRED_PACKAGES, **OPTIONAL_PACKAGES}.items():
        available, version = check_package(pkg)
        status[pkg] = (available, version)
        required = pkg in REQUIRED_PACKAGES
        if available:
            print(f"  [OK] {pkg} ({version}) - {desc} ready")
        else:
            tag = "MISSING" if required else "OPTIONAL"
            print(f"  [{tag}] {pkg} - {desc} not available")
            if required:
                all_ok = False

    if not all_ok:
        _print_install_instructions()

    return all_ok, status


def _print_install_instructions() -> None:
    print()
    print("DEPENDENCY ERROR: Required packages are missing.")
    print()
    print("Install with pip:")
    print("  pip install -r requirements.txt")
    print()
    print("Install with Poetry:")
    print("  poetry install")
    print("  poetry run python loading.py")


# ---------------------------------------------------------------------------
# Package version comparison
# ---------------------------------------------------------------------------

def show_package_comparison(status: dict[str, tuple[bool, str]]) -> None:
    """Compare installed versions between pip and Poetry contexts."""
    print()
    print("Package Management Comparison:")
    print(f"  {'Package':<14} {'Version':<12} {'Manager'}")
    print(f"  {'-'*14} {'-'*12} {'-'*20}")

    # Detect whether we're inside a Poetry-managed venv
    import os
    in_poetry = (
        os.environ.get("POETRY_ACTIVE") == "1"
        or "pypoetry" in sys.executable.lower()
        or (
            os.environ.get("VIRTUAL_ENV", "").find(".venv") != -1
            and os.path.exists(
                os.path.join(
                    os.path.dirname(os.path.dirname(sys.executable)), "pyproject.toml"
                )
            )
        )
    )
    manager = "Poetry" if in_poetry else "pip / system"

    all_pkgs = {**REQUIRED_PACKAGES, **OPTIONAL_PACKAGES}
    for pkg in all_pkgs:
        available, version = status.get(pkg, (False, ""))
        ver_str = version if available else "not installed"
        print(f"  {pkg:<14} {ver_str:<12} {manager}")

    print()
    print("  pip uses requirements.txt   -> declarative, flat version pins")
    print("  Poetry uses pyproject.toml  -> locked, reproducible dependency graph")


# ---------------------------------------------------------------------------
# Matrix data generation & analysis
# ---------------------------------------------------------------------------

def generate_matrix_data(n: int = 1000):  # type: ignore[return]
    """Generate simulated Matrix signal data using numpy exclusively."""
    import numpy as np  # noqa: PLC0415

    rng = np.random.default_rng(seed=42)

    time = np.linspace(0, 4 * np.pi, n)
    signal_a = np.sin(time) + rng.normal(0, 0.15, n)          # carrier wave
    signal_b = np.cos(time * 1.5) * rng.uniform(0.5, 1.5, n)  # modulated wave
    anomaly_mask = rng.random(n) > 0.97
    signal_a[anomaly_mask] += rng.normal(0, 2.0, anomaly_mask.sum())

    return time, signal_a, signal_b, anomaly_mask


def analyze_data(time, signal_a, signal_b, anomaly_mask):  # type: ignore[return]
    """Run basic statistical analysis with pandas + numpy."""
    import numpy as np   # noqa: PLC0415
    import pandas as pd  # noqa: PLC0415

    df = pd.DataFrame(
        {
            "time": time,
            "signal_a": signal_a,
            "signal_b": signal_b,
            "anomaly": anomaly_mask,
        }
    )

    stats = {
        "n_points": len(df),
        "n_anomalies": int(anomaly_mask.sum()),
        "signal_a_mean": float(np.mean(signal_a)),
        "signal_a_std": float(np.std(signal_a)),
        "signal_b_mean": float(np.mean(signal_b)),
        "signal_b_std": float(np.std(signal_b)),
        "correlation": float(df["signal_a"].corr(df["signal_b"])),
    }
    return df, stats


# ---------------------------------------------------------------------------
# Visualization
# ---------------------------------------------------------------------------

def generate_visualization(df, stats: dict, output_path: str = "matrix_analysis.png") -> None:
    """Render a Matrix-themed multi-panel chart."""
    import matplotlib.pyplot as plt          # noqa: PLC0415
    import matplotlib.gridspec as gridspec   # noqa: PLC0415
    import numpy as np                       # noqa: PLC0415

    BG = "#0d0d0d"
    GREEN = "#00ff41"
    CYAN = "#00e5ff"
    RED = "#ff003c"
    DIM = "#1a3a1a"

    fig = plt.figure(figsize=(14, 8), facecolor=BG)
    gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.45, wspace=0.35)

    ax_main = fig.add_subplot(gs[0, :])
    ax_hist = fig.add_subplot(gs[1, 0])
    ax_scatter = fig.add_subplot(gs[1, 1])

    for ax in (ax_main, ax_hist, ax_scatter):
        ax.set_facecolor(BG)
        for spine in ax.spines.values():
            spine.set_edgecolor(DIM)
        ax.tick_params(colors=GREEN, labelsize=7)
        ax.xaxis.label.set_color(GREEN)
        ax.yaxis.label.set_color(GREEN)
        ax.title.set_color(GREEN)

    # ── Main signal plot ──────────────────────────────────────────────────
    normal = ~df["anomaly"].values
    ax_main.plot(df["time"][normal], df["signal_a"][normal],
                 color=GREEN, lw=0.8, alpha=0.85, label="Signal A")
    ax_main.plot(df["time"][normal], df["signal_b"][normal],
                 color=CYAN, lw=0.8, alpha=0.65, label="Signal B")
    ax_main.scatter(df["time"][df["anomaly"]], df["signal_a"][df["anomaly"]],
                    color=RED, s=18, zorder=5, label=f"Anomalies ({stats['n_anomalies']})")
    ax_main.set_title("MATRIX SIGNAL FEED", fontsize=11, fontweight="bold", pad=10)
    ax_main.set_xlabel("Time")
    ax_main.set_ylabel("Amplitude")
    legend = ax_main.legend(framealpha=0.1, edgecolor=DIM, labelcolor="white", fontsize=8)
    legend.get_frame().set_facecolor(BG)

    # ── Histogram ────────────────────────────────────────────────────────
    ax_hist.hist(df["signal_a"], bins=50, color=GREEN, alpha=0.75, edgecolor=DIM)
    ax_hist.axvline(stats["signal_a_mean"], color=RED, lw=1.2, linestyle="--", label="mean")
    ax_hist.set_title("SIGNAL A DISTRIBUTION", fontsize=9, fontweight="bold")
    ax_hist.set_xlabel("Amplitude")
    ax_hist.set_ylabel("Count")
    legend2 = ax_hist.legend(framealpha=0.1, edgecolor=DIM, labelcolor="white", fontsize=7)
    legend2.get_frame().set_facecolor(BG)

    # ── Scatter ───────────────────────────────────────────────────────────
    sample = np.random.default_rng(0).integers(0, len(df), 300)
    ax_scatter.scatter(
        df["signal_a"].iloc[sample], df["signal_b"].iloc[sample],
        c=GREEN, s=6, alpha=0.55,
    )
    ax_scatter.set_title("A vs B CORRELATION", fontsize=9, fontweight="bold")
    ax_scatter.set_xlabel("Signal A")
    ax_scatter.set_ylabel("Signal B")

    corr_text = f"r = {stats['correlation']:.3f}"
    ax_scatter.text(
        0.97, 0.95, corr_text,
        transform=ax_scatter.transAxes, color=CYAN,
        fontsize=8, ha="right", va="top",
    )

    # ── Super-title & stats footer ────────────────────────────────────────
    fig.suptitle(
        "THE MATRIX — DATA ANALYSIS CONSTRUCT",
        color=GREEN, fontsize=14, fontweight="bold", y=0.98,
    )
    footer = (
        f"n={stats['n_points']}  |  "
        f"μ(A)={stats['signal_a_mean']:.3f}  σ(A)={stats['signal_a_std']:.3f}  |  "
        f"μ(B)={stats['signal_b_mean']:.3f}  σ(B)={stats['signal_b_std']:.3f}  |  "
        f"anomalies={stats['n_anomalies']}"
    )
    fig.text(0.5, 0.01, footer, ha="center", color="#445544", fontsize=7)

    plt.savefig(output_path, dpi=150, bbox_inches="tight", facecolor=BG)
    plt.close()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print()

    all_ok, status = check_dependencies()
    if not all_ok:
        sys.exit(1)

    show_package_comparison(status)

    print()
    print("Analyzing Matrix data...")
    time, signal_a, signal_b, anomaly_mask = generate_matrix_data(1000)
    print(f"Processing {len(time)} data points...")

    df, stats = analyze_data(time, signal_a, signal_b, anomaly_mask)

    print("Generating visualization...")
    output_path = "matrix_analysis.png"
    generate_visualization(df, stats, output_path)

    print("Analysis complete!")
    print(f"Results saved to: {output_path}")


if __name__ == "__main__":
    main()
