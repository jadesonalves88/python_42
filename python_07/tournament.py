from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex0.creatures import Creature
from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
)
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)


def _opponent_label(factory: CreatureFactory,
                    strategy: BattleStrategy) -> str:
    factory_name: str = type(factory).__name__
    strategy_name: str = type(strategy).__name__
    if "Strategy" in strategy_name:
        strategy_name = strategy_name.replace("Strategy", "")
    if "CreatureFactory" in factory_name:
        label: str = factory_name.replace("CreatureFactory", "")
    else:
        base: Creature = factory.create_base()
        label = base.name
    return f"{label}+{strategy_name}"


def _display_opponents(
    opponents: list[tuple[CreatureFactory, BattleStrategy]],
) -> str:
    parts: list[str] = [
        f"({_opponent_label(f, s)})" for f, s in opponents
    ]
    return ", ".join(parts)


def battle(opponents: list[tuple[CreatureFactory,
           BattleStrategy]]) -> None:
    print(f" [ {_display_opponents(opponents)} ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()

    n: int = len(opponents)
    for i in range(n):
        for j in range(i + 1, n):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]
            creature1: Creature = factory1.create_base()
            creature2: Creature = factory2.create_base()

            print("* Battle *")
            print(creature1.describe())
            print(" vs.")
            print(creature2.describe())
            print(" now fight!")

            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    flame_factory: FlameFactory = FlameFactory()
    healing_factory: HealingCreatureFactory = HealingCreatureFactory()
    normal_strategy: NormalStrategy = NormalStrategy()
    aggressive_strategy: AggressiveStrategy = AggressiveStrategy()
    defensive_strategy: DefensiveStrategy = DefensiveStrategy()

    print("Tournament 0 (basic)")
    battle([(flame_factory, normal_strategy),
            (healing_factory, defensive_strategy)])

    print()
    print("Tournament 1 (error)")
    battle([(flame_factory, aggressive_strategy),
            (healing_factory, defensive_strategy)])

    print()
    print("Tournament 2 (multiple)")
    aqua_factory: AquaFactory = AquaFactory()
    transform_factory: TransformCreatureFactory = \
        TransformCreatureFactory()
    battle([(aqua_factory, normal_strategy),
            (healing_factory, defensive_strategy),
            (transform_factory, aggressive_strategy)])
