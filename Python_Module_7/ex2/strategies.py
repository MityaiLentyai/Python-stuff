from abc import ABC, abstractmethod
from typing import cast

from ex0.creatures import Creature
from ex1.capabilities import TransformCapability, HealCapability


class BattleError(Exception):
    def __init__(self, creature_name: str, strategy_name: str):
        self.message = (
            f"Battle error, aborting tournament: "
            f"Invalid Creature '{creature_name}' for this "
            f"{strategy_name.split('Strategy', 1)[0].lower()} strategy"
        )
        super().__init__(self.message)


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    def validate(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise BattleError(creature.name, self.__class__.__name__)


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        self.validate(creature)
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        self.validate(creature)
        transformable = cast(TransformCapability, creature)  # To avoid mypy
        print(transformable.transform())
        print(creature.attack())
        print(transformable.revert())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        self.validate(creature)
        print(creature.attack())
        healer = cast(HealCapability, creature)
        print(healer.heal())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
