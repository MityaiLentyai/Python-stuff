import os
import sys
from dotenv import load_dotenv


def validate_config(mode: str, config_dict: dict[str, str]) -> None:
    for key, value in config_dict.items():
        clean_value = value.strip()

        if mode == "development":
            test_value = clean_value.replace(".", "").replace("-", "")
            if not test_value.isdigit():
                print(
                    f"❌ CONFIG ERROR [development]: "
                    f"Key '{key}' must be a numerical value. "
                    f"Found: '{value}'",
                    file=sys.stderr,
                )
                sys.exit(1)

        elif mode == "production":
            test_value = (
                clean_value.replace(" ", "")
                .replace("_", "")
                .replace("/", "")
                .replace(":", "")
                .replace(".", "")
                .replace("-", "")
            )
            if not test_value.isalpha():
                print(
                    f"❌ CONFIG ERROR [production]: "
                    f"Key '{key}' must contain only letters/text. "
                    f"Found: '{value}'",
                    file=sys.stderr,
                )
                sys.exit(1)


def main() -> None:
    if not os.path.exists(".env"):
        print("⚠️ WARNING: No '.env' file found in the current directory.")
        print("Falling back entirely to system environment variables.")
        sys.exit(1)
    else:
        print("✅ Found '.env' file. Loading configurations...")

    load_dotenv(override=False)

    matrix_mode = os.getenv("MATRIX_MODE")

    if not matrix_mode:
        print("❌ CRITICAL ERROR: MATRIX_MODE is missing!", file=sys.stderr)
        sys.exit(1)

    matrix_mode = matrix_mode.strip().lower()
    if matrix_mode not in ["development", "production"]:
        print(
            f"❌ CRITICAL ERROR: Invalid MATRIX_MODE '{matrix_mode}'. "
            f"Must be either 'development' or 'production'.",
            file=sys.stderr,
        )
        sys.exit(1)

    target_keys = ["DATABASE_URL", "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"]
    current_config = {key: os.getenv(key, "") for key in target_keys}

    for key, val in current_config.items():
        if not val:
            print(
                f"❌ CRITICAL ERROR: "
                f"Required configuration variable '{key}' is missing!",
                file=sys.stderr,
            )
            sys.exit(1)

    validate_config(matrix_mode, current_config)

    print("=== Oracle Matrix Shield Initiated ===")
    print(f"Environment Status: {matrix_mode.upper()}")
    print("Loaded configuration successfully:")
    for key, val in current_config.items():
        print(f" 🔹 {key}: {val}")


if __name__ == "__main__":
    main()
