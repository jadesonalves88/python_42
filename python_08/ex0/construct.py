import os
import site
import sys


def is_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def get_venv_name() -> str:
    venv_path = os.environ.get("VIRTUAL_ENV")
    if venv_path:
        return os.path.basename(venv_path)
    return os.path.basename(sys.prefix)


def get_package_paths() -> list[str]:
    try:
        return site.getsitepackages()
    except AttributeError:
        return [p for p in sys.path if "site-packages" in p]


def main() -> None:
    if is_virtual_env():
        venv_name = get_venv_name()
        venv_path = os.environ.get("VIRTUAL_ENV", sys.prefix)
        package_paths = get_package_paths()
        package_path_str = (
            package_paths[0] if package_paths else "unknown"
        )

        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_path}")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("Package installation path:")
        print(package_path_str)
    else:
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print("Then run this program again.")


if __name__ == "__main__":
    main()
