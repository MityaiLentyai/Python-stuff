from abc import ABC, abstractmethod

from ex0.creatures import Creature
from ex1.capabilities import TransformCapability, HealCapability


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature:Creature) -> None:
        creature.attack()

    def is_valid(self) -> bool:
        if isinstance(self, Creature):
            return True
        return False


class AggressiveStrategy(BattleStrategy):
    def act(self, creature:Creature) -> None:
        creature.transform()
        creature.attack()
        creature.revert()

    def is_valid(self) -> bool:
        if isinstance(self, TransformCapability):
            return True
        return False


class DefensiveStrategy(BattleStrategy):
    def act(self, creature:Creature) -> None:
        if self.is_valid():
            creature.attack()
            creature.heal()
        else:
            raise TypeError(
                f"Battle error, aborting tournament: Invalid Creature "
                f"'{creature.name}' for this aggressive strategy"
            )

    def is_valid(self) -> bool:
        if isinstance(self, HealCapability):
            return True
        return False
