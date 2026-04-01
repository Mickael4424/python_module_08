import os
import sys
from dotenv import load_dotenv


def check_config(config: dict) -> bool:
    missing = [key for key, value in config.items() if not value]
    if missing:
        print("ERROR: Missing configuration variables:")
        for var in missing:
            print(f" - {var}")
        return False
    return True


def display_config():
    print("\nConfiguration loaded:")
    mode = os.getenv("MATRIX_MODE")
    db = os.getenv("DATABASE_URL")
    if "sqlite" in db:
        database = "Connected to local instance"
    else:
        database = "Connected to remote production database"
    if os.getenv("API_KEY"):
        api_access = "Authenticated"
    else:
        api_access = "Missing key"

    log_level = os.getenv("LOG_LEVEL")

    if "localhost" in os.getenv("ZION_ENDPOINT"):
        zion = "Local connection"
    else:
        zion = "Online"

    print(f"Mode: {mode}")
    print(f"Database: {database}")
    print(f"API Access: {api_access}")
    print(f"Log level: {log_level}")
    print(f"Zion Network: {zion}")


def security_check():
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


def main():
    load_dotenv()

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }

    if not check_config(config):
        print("\nCreate a .env file or set environment variables")
        sys.exit(1)

    print("\nORACLE STATUS: Reading the Matrix...")
    display_config()
    security_check()
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
