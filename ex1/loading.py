import sys
import importlib


REQUIRED_LIBS = ["pandas", "requests", "numpy", "matplotlib"]


def is_venv() -> bool:
    return sys.prefix != sys.base_prefix


def get_env_info():
    return {
        "python_path": sys.executable,
        "venv": is_venv(),
        "venv_path": sys.prefix if is_venv() else None
    }


def check_dependency(lib_name: str):
    try:
        module = importlib.import_module(lib_name)
        version = getattr(module, "__version__", "unknown")
        return True, version
    except ImportError:
        return False, None


def check_all_dependencies():
    results = {}
    for lib in REQUIRED_LIBS:
        installed, version = check_dependency(lib)
        results[lib] = (installed, version)
    return results


def display_dependencies(results: dict) -> bool:
    print("\nChecking dependencies:")
    all_ok = True
    for lib, (installed, version) in results.items():
        if lib == "pandas":
            if installed:
                print(f"[OK] {lib} ({version}) - Data manipulation ready")
            else:
                print(f"Missing {lib}")
                all_ok = False
        elif lib == "requests":
            if installed:
                print(f"[OK] {lib} ({version}) - Network access ready")
            else:
                print(f"Missing {lib}")
                all_ok = False
        elif lib == "matplotlib":
            if installed:
                print(f"[OK] {lib} ({version}) - Visualization ready")
            else:
                print(f"Missing {lib}")
                all_ok = False
    return all_ok


def show_install_help():
    print("\nMissing dependencies detected.")
    print("Install with pip:")
    print("pip install -r requirements.txt")
    print("Or with Poetry:")
    print("poetry install")


def run_analysis():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("\nAnalysing Matrix data...")

    data = np.random.randn(1000)

    df = pd.DataFrame({"values": data})

    print(f"Processing {len(df)} data points...")
    min_val = df["values"].min()
    mean_val = df["values"].mean()
    max_val = df["values"].max()

    print(f"Min: {min_val:.1f}, Mean {mean_val:.1f}, Max: {max_val:.1f}")

    print("Generating visualization...")
    plt.hist(df["values"], bins=30)
    plt.title("Matrix Data")

    output = "matrix_analysis.png"
    plt.savefig(output)

    print("\nAnalysis completed!")
    print(f"Results saved to: {output}")


def main():

    print("\nLOADING STATUS: Loading programs...")

    results = check_all_dependencies()
    all_ok = display_dependencies(results)
    if not all_ok:
        show_install_help()
        sys.exit(1)
    run_analysis()


if __name__ == "__main__":
    main()
