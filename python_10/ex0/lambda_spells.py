"""Lambda Sanctum: master anonymous functions with lambda expressions."""


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort magical artifacts by power level in descending order."""
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Return the mages whose power is at least ``min_power``."""
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Wrap every spell name with a '* ' prefix and a ' *' suffix."""
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Return the max, min and average power of a group of mages."""
    return {
        "max_power": max(mages, key=lambda m: m["power"])["power"],
        "min_power": min(mages, key=lambda m: m["power"])["power"],
        "avg_power": round(
            sum(map(lambda m: m["power"], mages)) / len(mages), 2
        ),
    }


def main() -> None:
    """Demonstrate every lambda spell of the Sanctum."""
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Rune Blade", "power": 78, "type": "sword"},
    ]
    mages = [
        {"name": "Alex", "power": 92, "element": "fire"},
        {"name": "Jordan", "power": 45, "element": "water"},
        {"name": "Riley", "power": 68, "element": "earth"},
    ]
    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    ordered = artifact_sorter(artifacts)
    first, second = ordered[0], ordered[1]
    print(
        f"{first['name']} ({first['power']} power) comes before "
        f"{second['name']} ({second['power']} power)"
    )

    print("\nTesting power filter...")
    strong = power_filter(mages, 60)
    print(
        "Strong mages: "
        + ", ".join(f"{m['name']} ({m['power']})" for m in strong)
    )

    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(
        f"max_power: {stats['max_power']}, "
        f"min_power: {stats['min_power']}, "
        f"avg_power: {stats['avg_power']}"
    )


if __name__ == "__main__":
    main()
