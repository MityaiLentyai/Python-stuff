from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str = "Unknown creature",
                 creature_type: str = "Unknown type") -> None:
        self.name = name
        self.type = creature_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    def __init__(self, name: str = "Flameling") -> None:
        super().__init__(name=name, creature_type="Fire")

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self, name: str = "Pyrodon") -> None:
        super().__init__(name=name, creature_type="Fire/Flying")

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self, name: str = "Aquabub") -> None:
        super().__init__(name=name, creature_type="Water")

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    def __init__(self, name: str = "Torragon") -> None:
        super().__init__(name=name, creature_type="Water")

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"
