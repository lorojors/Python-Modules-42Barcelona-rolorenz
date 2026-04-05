from __future__ import annotations

import os
import site
import sys


def is_virtual_environment() -> bool:
    if hasattr(sys, "real_prefix"):
        return True
    if sys.prefix != getattr(sys, "base_prefix", sys.prefix):
        return True
    if os.environ.get("VIRTUAL_ENV"):
        return True
    return False


def get_venv_name() -> str | None:
    virtual_env = os.environ.get("VIRTUAL_ENV")
    if virtual_env:
        return os.path.basename(virtual_env)
    return None


def get_site_packages() -> str:
    try:
        packages = site.getsitepackages()
        return packages[0] if packages else "Unknown"
    except AttributeError:
        return site.getusersitepackages()


def get_activation_instructions() -> str:
    lines = [
        "    python -m venv matrix_env",
        "    source matrix_env/bin/activate  # On Unix",
        r"    matrix_env\Scripts\activate     # On Windows",
    ]
    return "\n".join(lines)


def print_outside_venv() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print(get_activation_instructions())
    print()
    print("Then run this program again.")


def print_inside_venv() -> None:
    venv_name = get_venv_name() or os.path.basename(sys.prefix)
    venv_path = os.environ.get("VIRTUAL_ENV", sys.prefix)
    site_packages = get_site_packages()

    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print()
    print(f"Package installation path: {site_packages}")


def main() -> None:
    inside_venv = is_virtual_environment()

    if inside_venv:
        print("Inside the Construct")
        print()
        print_inside_venv()
    else:
        print("Outside the Matrix")
        print()
        print_outside_venv()


if __name__ == "__main__":
    main()