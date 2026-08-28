from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex0.creatures import Creature


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base: Creature = factory.create_base()
    evolved: Creature = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())
    print()


def battle_factories(factory1: CreatureFactory,
                     factory2: CreatureFactory) -> None:
    print("Testing battle")
    creature1: Creature = factory1.create_base()
    creature2: Creature = factory2.create_base()
    print(creature1.describe())
    print(" vs.")
    print(creature2.describe())
    print(" fight!")
    print(creature1.attack())
    print(creature2.attack())


if __name__ == "__main__":
    flame_factory: FlameFactory = FlameFactory()
    aqua_factory: AquaFactory = AquaFactory()
    test_factory(flame_factory)
    test_factory(aqua_factory)
    battle_factories(flame_factory, aqua_factory)
