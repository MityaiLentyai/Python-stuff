from ex0.creatures import Creature
from ex1.capabilities import HealCapability, \
    TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str = "Sproutling") -> None:
        super().__init__(name=name, creature_type="Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: str = "itself") -> str:
        return f"{self.name} heals {target} for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str = "Bloomelle") -> None:
        super().__init__(name=name, creature_type="Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: str = "itself and others") -> str:
        return f"{self.name} heals {target} for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str = "Shiftling") -> None:
        super().__init__(name=name, creature_type="Normal", )
        self.shifted: bool = False

    def attack(self) -> str:
        if not self.shifted:
            return f"{self.name} attacks normally."
        return f"{self.name} performs a boosted strike!"

    def transform(self) -> str:
        self.shifted = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.shifted = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str = "Morphagon") -> None:
        super().__init__(name=name, creature_type="Normal/Dragon")
        self.shifted: bool = False

    def attack(self) -> str:
        if not self.shifted:
            return f"{self.name} attacks normally."
        return f"{self.name}  unleashes a devastating morph strike!"

    def transform(self) -> str:
        self.shifted = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.shifted = False
        return f"{self.name} stabilizes its form"
