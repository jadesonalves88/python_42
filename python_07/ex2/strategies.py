from abc import ABC, abstractmethod

from ex0.creatures import Creature
from ex1.creatures import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        self._name = "normal"

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}'"
                f" for this {self._name} strategy"
            )
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        self._name = "aggressive"

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}'"
                f" for this {self._name} strategy"
            )
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        self._name = "defensive"

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}'"
                f" for this {self._name} strategy"
            )
        print(creature.attack())
        if isinstance(creature, HealCapability):
            print(creature.heal())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
