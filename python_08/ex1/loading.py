import importlib
import sys


REQUIRED_PACKAGES = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}

OPTIONAL_PACKAGES = {
    "requests": "Network access ready",
}


def check_package(package_name: str) -> tuple[bool, str]:
    try:
        module = importlib.import_module(package_name)
        version = getattr(module, "__version__", "unknown")
        return True, str(version)
    except ImportError:
        return False, ""


def check_dependencies() -> dict[str, tuple[bool, str, str]]:
    results: dict[str, tuple[bool, str, str]] = {}

    for pkg, description in {
        **REQUIRED_PACKAGES,
        **OPTIONAL_PACKAGES,
    }.items():
        available, version = check_package(pkg)
        results[pkg] = (available, version, description)

    return results


def print_dependency_status(
    results: dict[str, tuple[bool, str, str]]
) -> list[str]:
    missing: list[str] = []

    for pkg, (available, version, description) in results.items():
        if available:
            print(f"[OK] {pkg} ({version}) - {description}")
        else:
            if pkg in REQUIRED_PACKAGES:
                print(f"[MISSING] {pkg} - {description}")
                missing.append(pkg)
            else:
                print(f"[--] {pkg} - {description} (optional)")

    return missing


def show_install_instructions(missing: list[str]) -> None:
    if not missing:
        return

    print("\nMissing dependencies detected!")
    print("\nTo install with pip:")
    print("  pip install -r requirements.txt")
    print("\nTo install with Poetry:")
    print("  poetry install")
    print("  poetry run python loading.py")
    print("\n  Check pyproject.toml and requirements.txt for exact versions.")

    print("\nPip vs Poetry - Key differences:")
    print("  • Pip: Simple package installer, uses requirements.txt")
    print("  • Poetry: Full dependency manager, uses pyproject.toml")
    print(
        "  • Poetry locks exact versions (poetry.lock),"
        " pip does not by default"
    )
    print("  • Poetry creates virtual environments automatically")
    print("  • Pip installs globally unless you manage venvs manually")


def run_analysis() -> None:
    import matplotlib  # type: ignore[import]
    matplotlib.use("Agg")

    import numpy as np  # type: ignore[import]
    import pandas as pd  # type: ignore[import]
    import matplotlib.pyplot as plt  # type: ignore[import]

    np.random.seed(42)
    n_samples = 1000

    print("\nAnalyzing Matrix data...")

    sentinels = np.random.randn(n_samples) * 3 + 15
    agents = np.random.randn(n_samples) * 5 + 10
    redpills = np.random.randn(n_samples) * 2 + 12

    df = pd.DataFrame({
        "Sentinels": sentinels,
        "Agents": agents,
        "Redpills": redpills,
    })

    print(f"Processing {len(df)} data points...")

    stats = df.describe()

    print("\nSimulated Matrix Battle Statistics:")
    print(stats.to_string())

    print("\nGenerating visualization...")

    _, axes = plt.subplots(1, 3, figsize=(15, 5))

    axes[0].hist(
        df["Sentinels"],
        bins=30,
        color="red",
        alpha=0.7,
        edgecolor="black",
    )
    axes[0].set_title("Sentinels Distribution")
    axes[0].set_xlabel("Power Level")

    axes[1].hist(
        df["Agents"],
        bins=30,
        color="blue",
        alpha=0.7,
        edgecolor="black",
    )
    axes[1].set_title("Agents Distribution")
    axes[1].set_xlabel("Power Level")

    axes[2].hist(
        df["Redpills"],
        bins=30,
        color="green",
        alpha=0.7,
        edgecolor="black",
    )
    axes[2].set_title("Redpills Distribution")
    axes[2].set_xlabel("Power Level")

    plt.tight_layout()
    try:
        plt.savefig("matrix_analysis.png", dpi=100)
    except OSError as e:
        print(f"ERROR: Could not save visualization: {e}")
        sys.exit(1)
    finally:
        plt.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")

    print("\nPip vs Poetry comparison (installed via importlib):")

    for pkg in ["pandas", "numpy", "matplotlib"]:
        mod = importlib.import_module(pkg)
        ver = getattr(mod, "__version__", "unknown")

        print(f"  {pkg} == {ver}  # pip format")
        print(f'  {pkg} = "^{ver}"  # poetry format (approximate)')


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    results = check_dependencies()
    missing = print_dependency_status(results)

    if missing:
        show_install_instructions(missing)
        sys.exit(1)

    run_analysis()


if __name__ == "__main__":
    main()
