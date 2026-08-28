"""Master's Tower: decorators and class methods."""

import time
from collections.abc import Callable
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    """Decorate a spell to measure and report its execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    """Decorate a spell to reject power levels below ``min_power``."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power", args[-1] if args else None)
            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Decorate a spell to retry up to ``max_attempts`` times on failure."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    """A guild of mages with validated names and powered spells."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Return True if the name is at least 3 letters/spaces long."""
        return len(name) >= 3 and all(
            char.isalpha() or char.isspace() for char in name
        )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell, requiring at least 10 power."""
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    """Demonstrate the decorators and the MageGuild class."""
    print("Testing spell timer...")

    @spell_timer
    def fireball(target: str) -> str:
        time.sleep(0.1)
        return f"Fireball cast at {target}!"

    print(f"Result: {fireball('Dragon')}")

    print("\nTesting power validator...")

    @power_validator(10)
    def firebolt(target: str, power: int) -> str:
        return f"Firebolt hits {target} for {power} damage"

    print(firebolt("Goblin", 25))
    print(firebolt("Goblin", 5))

    print("\nTesting retrying spell...")

    @retry_spell(3)
    def miscast() -> str:
        raise RuntimeError("the spell backfired")

    print(miscast())

    tries = {"count": 0}

    @retry_spell(3)
    def waaagh() -> str:
        tries["count"] += 1
        if tries["count"] < 3:
            raise RuntimeError("not enough fury")
        return "Waaaaaaagh spelled !"

    print(waaagh())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Riley"))
    print(guild.validate_mage_name("R1"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Ember", 5))


if __name__ == "__main__":
    main()
