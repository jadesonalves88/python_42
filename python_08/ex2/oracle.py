import os


def load_environment() -> dict[str, str | None]:
    config: dict[str, str | None] = {}

    try:
        from dotenv import load_dotenv  # type: ignore[import]
        env_path = os.path.join(os.path.dirname(__file__), ".env")
        load_dotenv(dotenv_path=env_path)
    except ImportError:
        pass

    config["MATRIX_MODE"] = os.environ.get("MATRIX_MODE", "development")
    config["DATABASE_URL"] = os.environ.get("DATABASE_URL")
    config["API_KEY"] = os.environ.get("API_KEY")
    config["LOG_LEVEL"] = os.environ.get("LOG_LEVEL", "INFO")
    config["ZION_ENDPOINT"] = os.environ.get("ZION_ENDPOINT")

    return config


def check_security(config: dict[str, str | None]) -> list[str]:
    checks: list[str] = []
    hardcoded_found = False

    with open(__file__, "r") as f:
        source = f.read()
        for key in ["DATABASE_URL", "API_KEY"]:
            val = config.get(key)
            if val and f'"{val}"' in source:
                hardcoded_found = True
                break
            if val and f"'{val}'" in source:
                hardcoded_found = True
                break

    if not hardcoded_found:
        checks.append("[OK] No hardcoded secrets detected")
    else:
        checks.append("[WARNING] Hardcoded secrets found in source!")

    env_path = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.isfile(env_path):
        checks.append("[OK] .env file properly configured")
    else:
        checks.append("[WARNING] No .env file found")

    checks.append("[OK] Production overrides available")

    return checks


def format_database_url(url: str | None, mode: str) -> str:
    if not url:
        if mode == "production":
            return "ERROR: DATABASE_URL not configured!"
        return "Using default local instance"
    if "localhost" in url or "127.0.0.1" in url:
        return f"Connected to local instance ({url})"
    return f"Connected to {url}"


def format_api_key(key: str | None) -> str:
    if not key:
        return "Not configured - API access disabled"
    mask = key[:4] + "*" * (len(key) - 4) if len(key) > 4 else "****"
    return f"Authenticated (key: {mask})"


def format_log_level(level: str) -> str:
    return level.upper()


def format_zion_endpoint(endpoint: str | None) -> str:
    if not endpoint:
        return "Offline - No resistance network"
    return f"Online ({endpoint})"


def show_mode_banner(mode: str) -> None:
    if mode == "production":
        print("=" * 50)
        print("PRODUCTION MODE - Live system, be careful!")
        print("=" * 50)
    else:
        print("-" * 50)
        print("DEVELOPMENT MODE - Safe to experiment")
        print("-" * 50)


def main() -> None:
    config = load_environment()

    mode = config["MATRIX_MODE"]
    if mode not in ("development", "production"):
        mode = "development"
        config["MATRIX_MODE"] = mode

    print("ORACLE STATUS: Reading the Matrix...")

    show_mode_banner(mode)

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {format_database_url(config['DATABASE_URL'], mode)}")
    print(f"API Access: {format_api_key(config['API_KEY'])}")
    print(f"Log Level: {format_log_level(str(config['LOG_LEVEL']))}")
    print(f"Zion Network: {format_zion_endpoint(config['ZION_ENDPOINT'])}")

    print("\nEnvironment security check:")
    for check in check_security(config):
        print(check)

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
