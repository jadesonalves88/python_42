from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.creatures import (
    Bloomelle,
    Morphagon,
    Shiftling,
    Sproutling,
)


def test_healing(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    base: Sproutling = factory.create_base()
    evolved: Bloomelle = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform(factory: TransformCreatureFactory) -> None:
    print()
    print("Testing Creature with transform capability")
    print(" base:")
    base: Shiftling = factory.create_base()
    evolved: Morphagon = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    healing_factory: HealingCreatureFactory = HealingCreatureFactory()
    test_healing(healing_factory)
    transform_factory: TransformCreatureFactory = TransformCreatureFactory()
    test_transform(transform_factory)
