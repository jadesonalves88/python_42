import random


ACHIEVEMENTS: list[str] = [
    "First Steps", "Master Explorer", "Crafting Genius",
    "Boss Slayer", "Treasure Hunter", "Untouchable",
    "Speed Runner", "Strategist", "Unstoppable",
    "Collector Supreme", "World Savior", "Sharp Mind",
    "Survivor", "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    count: int = random.randint(4, 9)
    return set(random.sample(ACHIEVEMENTS, count))


def main() -> None:
    players: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]
    achievements: dict[str, set[str]] = {}

    for player in players:
        achievements[player] = gen_player_achievements()

    print("=== Achievement Tracker System ===")
    for player in players:
        print(f"Player {player}: {achievements[player]}")

    all_achievements: set[str] = set()
    for player in players:
        all_achievements = all_achievements.union(achievements[player])
    print(f"All distinct achievements: {all_achievements}")

    common: set[str] = set(ACHIEVEMENTS)
    for player in players:
        common = common.intersection(achievements[player])
    print(f"Common achievements: {common}")

    for player in players:
        others: set[str] = set()
        for other in players:
            if other != player:
                others = others.union(achievements[other])
        only_player: set[str] = achievements[player].difference(others)
        print(f"Only {player} has: {only_player}")

    all_set: set[str] = set(ACHIEVEMENTS)
    for player in players:
        missing: set[str] = all_set.difference(achievements[player])
        print(f"{player} is missing: {missing}")


if __name__ == "__main__":
    main()
