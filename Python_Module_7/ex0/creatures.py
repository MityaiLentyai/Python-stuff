from abc import ABC, abstractmethod
import typing

class Creature(ABC):
    def __init__(self, name: str, creature_type: str):
        self.name = name
        self.type = creature_type  # Holds the generic type attribute

    @abstractmethod
    def attack(self) -> None:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"

class Flameling(Creature):
    def attack(self) -> str:
        