import sys
import os
import site


def check_matrix_status() -> None:
    try:
        in_venv = sys.prefix != sys.base_prefix

        if in_venv:
            print("\nMATRIX STATUS: Welcome to the construct")

            print(f"\nCurrent Python: {sys.executable}")
            env_name = os.path.basename(sys.prefix)
            print(f"Virtual Environment: {env_name}")
            print(f"Environment Path: {sys.prefix}")

            print("\nSUCCESS: You're in an isolated environment!")
            print("Safe to install packages without "
                  "affecting the global system.")

            print("\nPackage installation path:")
            packages_path = site.getsitepackages()[0]
            print(f"{packages_path}")

        else:
            print("\nMATRIX STATUS: You're still plugged in")

            print(f"\nCurrent Python: {sys.executable}")
            print("Virtual Environment: None detected")

            print("\nWARNING: You're in the global environment!")
            print("The machines can see everything you install.")

            print("\nTo enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate # On Unix")
            print("matrix_env")
            print("Scripts")
            print("activate # On Windows")

            print("\nThen run this program again.")

    except Exception as e:
        print(f"Error accessing the matrix: {e}")


def main():
    check_matrix_status()


if __name__ == "__main__":
    main()
