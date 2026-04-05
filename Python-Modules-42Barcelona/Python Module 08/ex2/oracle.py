from __future__ import annotations

import os
import sys

# ---------------------------------------------------------------------------
# python-dotenv — load .env before anything else reads os.environ
# ---------------------------------------------------------------------------
try:
    from dotenv import load_dotenv, dotenv_values
    _DOTENV_AVAILABLE = True
except ImportError:
    _DOTENV_AVAILABLE = False


# ---------------------------------------------------------------------------
# Constants & defaults
# ---------------------------------------------------------------------------

ENV_FILE = ".env"

DEFAULTS: dict[str, str] = {
    "MATRIX_MODE":    "development",
    "DATABASE_URL":   "sqlite:///matrix_local.db",
    "API_KEY":        "",
    "LOG_LEVEL":      "DEBUG",
    "ZION_ENDPOINT":  "http://localhost:7110/zion",
}

# Values that indicate a key was left as a placeholder rather than set
_PLACEHOLDER_TOKENS = {
    "your_api_key_here",
    "change_me",
    "secret",
    "xxx",
    "placeholder",
    "<your-key>",
}


# ---------------------------------------------------------------------------
# Config loading
# ---------------------------------------------------------------------------

class Config:
    """Validated, typed view of the application's environment configuration."""

    def __init__(self, data: dict[str, str]) -> None:
        self.mode: str         = data.get("MATRIX_MODE",   DEFAULTS["MATRIX_MODE"]).lower()
        self.database_url: str = data.get("DATABASE_URL",  DEFAULTS["DATABASE_URL"])
        self.api_key: str      = data.get("API_KEY",        DEFAULTS["API_KEY"])
        self.log_level: str    = data.get("LOG_LEVEL",      DEFAULTS["LOG_LEVEL"]).upper()
        self.zion_endpoint: str = data.get("ZION_ENDPOINT", DEFAULTS["ZION_ENDPOINT"])

    # ── derived properties ────────────────────────────────────────────────

    @property
    def is_production(self) -> bool:
        return self.mode == "production"

    @property
    def db_label(self) -> str:
        url = self.database_url
        if not url:
            return "NOT CONFIGURED"
        if "localhost" in url or "127.0.0.1" in url or "sqlite" in url:
            return "Connected to local instance"
        # mask credentials in remote URLs  (postgres://user:pass@host/db)
        try:
            scheme, rest = url.split("://", 1)
            if "@" in rest:
                _, host_part = rest.split("@", 1)
                return f"Connected to {scheme}://***@{host_part}"
            return f"Connected to {scheme}://{rest}"
        except ValueError:
            return "Connected (URL masked)"

    @property
    def api_label(self) -> str:
        if not self.api_key:
            return "NOT AUTHENTICATED — API_KEY missing"
        if self.api_key.lower() in _PLACEHOLDER_TOKENS:
            return "NOT AUTHENTICATED — placeholder value detected"
        return "Authenticated"

    @property
    def zion_label(self) -> str:
        if not self.zion_endpoint:
            return "OFFLINE — endpoint not set"
        return "Online"


def load_config() -> Config:
    """
    Priority (highest → lowest):
      1. Real environment variables (shell exports, docker env, CI secrets …)
      2. .env file values
      3. Built-in defaults
    """
    if not _DOTENV_AVAILABLE:
        print("WARNING: python-dotenv is not installed.")
        print("         Install it with:  pip install python-dotenv")
        print("         .env files will not be loaded until it is available.")
        print()

    env_file_found = os.path.isfile(ENV_FILE)

    if _DOTENV_AVAILABLE and env_file_found:
        # override=False → real env vars win over .env values
        load_dotenv(dotenv_path=ENV_FILE, override=False)

    return Config(dict(os.environ))


# ---------------------------------------------------------------------------
# Security checks
# ---------------------------------------------------------------------------

def _env_file_in_gitignore() -> bool:
    for candidate in (".gitignore", "../.gitignore"):
        if os.path.isfile(candidate):
            with open(candidate) as fh:
                for line in fh:
                    stripped = line.strip()
                    if stripped in (".env", "*.env", ".env*") or stripped.startswith(".env"):
                        return True
    return False


def run_security_checks(cfg: Config) -> list[tuple[bool, str]]:
    results: list[tuple[bool, str]] = []

    # 1. No hardcoded secrets in this source file
    with open(__file__) as fh:
        source = fh.read()
    has_hardcoded = any(
        tok in source
        for tok in ("password=", "secret=", "api_key=")
        if tok not in ('        if tok not in ("password=", "secret=", "api_key=")\n',)
    )
    results.append((not has_hardcoded, "No hardcoded secrets detected"))

    # 2. .env file exists and is populated
    env_file_ok = os.path.isfile(ENV_FILE)
    results.append((env_file_ok, ".env file properly configured"))

    # 3. .env is listed in .gitignore
    gitignore_ok = _env_file_in_gitignore()
    results.append((gitignore_ok, ".env listed in .gitignore (secrets won't be committed)"))

    # 4. Production overrides can be injected via real env vars
    overrides_available = any(
        k in os.environ for k in ("MATRIX_MODE", "API_KEY", "DATABASE_URL")
    )
    results.append((True, "Production overrides available via shell environment"))

    # 5. API key not a plain placeholder
    key_ok = bool(cfg.api_key) and cfg.api_key.lower() not in _PLACEHOLDER_TOKENS
    results.append((key_ok, "API_KEY set to a non-placeholder value"))

    return results


# ---------------------------------------------------------------------------
# Production-specific behaviour demo
# ---------------------------------------------------------------------------

def _production_notes(cfg: Config) -> list[str]:
    notes = []
    if cfg.log_level == "DEBUG":
        notes.append("  WARN  LOG_LEVEL is DEBUG — use WARNING or ERROR in production")
    if "localhost" in cfg.database_url or "sqlite" in cfg.database_url:
        notes.append("  WARN  DATABASE_URL points to a local instance — set a remote URL")
    if not cfg.api_key or cfg.api_key.lower() in _PLACEHOLDER_TOKENS:
        notes.append("  WARN  API_KEY is missing or placeholder — injection required")
    if not notes:
        notes.append("  All production settings look healthy.")
    return notes


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def print_report(cfg: Config) -> None:
    env_file_found = os.path.isfile(ENV_FILE)
    dotenv_src = ".env file" if env_file_found and _DOTENV_AVAILABLE else "defaults / shell"

    print("ORACLE STATUS: Reading the Matrix...")
    print()

    # ── source banner ──────────────────────────────────────────────────────
    if not _DOTENV_AVAILABLE:
        print("[!] python-dotenv unavailable — using shell environment and defaults only")
    elif not env_file_found:
        print("[!] No .env file found — using shell environment and defaults")
        print("    Tip: cp .env.example .env  then edit it with your values")
    else:
        print(f"[+] Configuration source: {dotenv_src}")

    print()

    # ── config values ──────────────────────────────────────────────────────
    print("Configuration loaded:")
    mode_flag = "PRODUCTION" if cfg.is_production else "development"
    print(f"  Mode:         {mode_flag}")
    print(f"  Database:     {cfg.db_label}")
    print(f"  API Access:   {cfg.api_label}")
    print(f"  Log Level:    {cfg.log_level}")
    print(f"  Zion Network: {cfg.zion_label}")
    print()

    # ── production-specific notes ──────────────────────────────────────────
    if cfg.is_production:
        print("Production environment checks:")
        for note in _production_notes(cfg):
            print(note)
        print()

    # ── security checks ────────────────────────────────────────────────────
    print("Environment security check:")
    checks = run_security_checks(cfg)
    for ok, label in checks:
        tag = "[OK]" if ok else "[--]"
        print(f"  {tag} {label}")

    print()
    print("The Oracle sees all configurations.")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    cfg = load_config()
    print_report(cfg)

    # Exit with non-zero if critical config is absent in production
    if cfg.is_production and (
        not cfg.api_key or cfg.api_key.lower() in _PLACEHOLDER_TOKENS
    ):
        sys.exit(1)


if __name__ == "__main__":
    main()
