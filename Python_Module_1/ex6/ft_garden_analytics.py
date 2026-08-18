#!/usr/bin/env python3


class Plant:

    class _PlantStats:

        def __init__(self):
            self._grow_count: int = 0
            self._age_count: int = 0
            self._show_count: int = 0

        def display(self, plant_name: str) -> None:
            print(f"[statisics for {plant_name.capitalize()}]")
            print(
                f"Stats: {self._grow_count} grow, {self._age_count} age, "
                f"{self._show_count} show"
            )

    def __init__(self, _name: str, _height: float, _age_days: int):
        self._name = _name
        if _height >= 0:
            self._height = _height
        else:
            self._height = 0.0  # How else am I supposed to handle it?
            print(
                f"{self._name.capitalize()}: Error, height can't be negative."
                f" Defaulting to 0.0cm"
            )
        if _age_days >= 0:
            self._age_days = _age_days
        else:
            self._age_days = 0  # Same
            print(
                f"{self._name.capitalize()}: Error, age can't be negative."
                f" Defaulting to 0 days"
            )

        self._stats = self._PlantStats()

    @staticmethod
    def is_older_than_a_year(days: int) -> bool:
        if days > 365:
            return True
        else:
            return False

    @classmethod
    def create_preps(cls, _height: float = 0.0, _age_days: int = 0):
        return cls(_name="Unknown plant", _height=_height, _age_days=_age_days)

    def show(self) -> None:
        self._stats._show_count += 1
        print(
            f"{self._name.capitalize()}: {self._height}cm, "
            f"{self._age_days} days old"
        )

    def age(self):
        self._stats._grow_count += 1
        self._age_days += 1

    def grow(self):
        self._stats._grow_count += 1
        self._height = round(self._height * 1.119, 1)

    def display_stats(self) -> None:
        self._stats.display(self._name)


class Flower(Plant):
    # fmt: off
    def __init__(
        self, _name: str, _height: float, _age_days: int,
        _color: str, _is_bloomed: bool
    ):
        super().__init__(_name, _height, _age_days)
        self._color = _color
        self._is_bloomed = _is_bloomed
    # fmt: on

    def grow(self):
        self._height += 8
        self._stats._grow_count += 1

    def show(self):
        super().show()
        print(f" Color: {self._color}")
        if self._is_bloomed:
            print(f" {self._name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self._name.capitalize()} has not bloomed yet")

    def bloom(self):
        self._is_bloomed = True


class Seed(Flower):
    def __init__(
        self,
        _name: str,
        _height: float,
        _age_days: int,
        _color: str,
        _is_bloomed: bool,
        _seed_count: int,
    ):
        super().__init__(_name, _height, _age_days, _color, _is_bloomed)
        self._seed_count = _seed_count

    def bloom(self):
        super().bloom()
        self._seed_count += 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seed_count}")

    def grow(self) -> None:
        self._height += 30
        self._stats._grow_count += 1

    def age(self) -> None:
        self._age_days += 20
        self._stats._age_count += 1


class Tree(Plant):
    # fmt: off
    def __init__(
        self, _name: str, _height: float, _age_days: int,
        _trunk_diameter: float, _shades_produced: int
    ):
        super().__init__(_name, _height, _age_days)
        self._shades_produced = _shades_produced
        self._trunk_diameter = _trunk_diameter
    # fmt: on

    def produce_shade(self) -> None:
        print("[asking the oak to produce shade]")
        self._shades_produced += 1
        print(
            f"Tree {self._name} now produces a shade of {self._height}cm "
            f"long and {self._trunk_diameter} wide."
        )

    def display_stats(self) -> None:
        super().display_stats()
        print(f" {self._shades_produced} shade")

    def show(self):
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}")


class Vegetable(Plant):
    # fmt: off
    def __init__(
        self, _name: str, _height: float, _age_days: int,
        _harvest_season: str, _nutritional_value: int
    ):
        super().__init__(_name, _height, _age_days)

        self._harvest_season = _harvest_season
        self._nutritional_value = _nutritional_value
    # fmt: on

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


def display_stats(self):
    self.display_stats()


def main() -> None:

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print("Is 400 days more than a year? -> ", end="")
    print(f"{Plant.is_older_than_a_year(400)}")
    print()

    # fmt: off
    rose = Flower(
        _name="Rose",
        _height=15.0,
        _age_days=10,
        _color="red",
        _is_bloomed=False
    )
    oak = Tree(
        _name="Oak",
        _height=200.0,
        _trunk_diameter=5.0,
        _age_days=365,
        _shades_produced=0
        )
    seed = Seed(
        _name="Sunflower",
        _height=80.0,
        _age_days=45,
        _color="yellow",
        _is_bloomed=False,
        _seed_count=0
    )
    anonymous = Plant.create_preps()

    # fmt: on
    print(f"=== {rose.__class__.__name__.capitalize()}")

    rose.show()
    rose.display_stats()
    print("[asking the rose to grow and bloom]")
    rose.bloom()
    rose.grow()
    rose.show()
    rose.display_stats()
    print()

    print(f"=== {oak.__class__.__name__.capitalize()}")
    oak.show()
    oak.display_stats()
    oak.produce_shade()
    oak.display_stats()
    print()

    print(f"=== {seed.__class__.__name__.capitalize()}")
    seed.show()
    print(f"[make {seed._name.lower()} grow, age and bloom]")
    seed.bloom()
    seed.grow()
    seed.age()
    seed.show()
    seed.display_stats()
    print()

    print(f"=== {anonymous.__class__.__name__.capitalize()}")
    anonymous.show()
    display_stats(anonymous)


if __name__ == "__main__":
    main()
