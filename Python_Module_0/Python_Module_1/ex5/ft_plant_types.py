#!/usr/bin/env python3


class Plant:

    def __init__(self, _name: str, _height: float, _age_days: int):
        self._name: str = _name
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

    def show(self) -> None:
        print(
            f"{self._name.capitalize()}: {self._height}cm, "
            f"{self._age_days} days old"
        )

    def age(self):
        self._age_days += 1

    def grow(self):
        self._height = round(self._height * 1.119, 1)


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

    def show(self):
        super().show()
        print(f" Color: {self._color}")
        if self._is_bloomed:
            print(f" {self._name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self._name.capitalize()} has not bloomed yet")

    def bloom(self):
        print("[asking the rose to bloom]")
        self._is_bloomed = True


class Tree(Plant):
    # fmt: off
    def __init__(
        self, _name: str, _height: float, _age_days: int,
        _trunk_diameter: float,
    ):
        super().__init__(_name, _height, _age_days)

        self._trunk_diameter = _trunk_diameter
    # fmt: on

    def produce_shade(self) -> None:
        print("[asking the oak to produce shade]")
        print(
            f"Tree {self._name} now produces a shade of {self._height}cm "
            f"long and {self._trunk_diameter} wide"
        )

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


def main() -> None:

    print("=== Garden Plant Types ===")
    # fmt: off
    rose = Flower(
        _name="Rose", _height=15.0, _age_days=10,
        _color="red", _is_bloomed=False
    )
    oak = Tree(_name="Oak", _height=200.0, _trunk_diameter=5.0, _age_days=45)
    tomato = Vegetable(
        _name="Tomato",
        _height=5.0,
        _age_days=10,
        _harvest_season="April",
        _nutritional_value=0,
    )
    # fmt: on
    print(f"=== {rose.__class__.__name__.capitalize()}")

    rose.show()
    rose.bloom()
    rose.show()
    print()

    print(f"=== {oak.__class__.__name__.capitalize()}")
    oak.show()
    oak.produce_shade()
    print()

    print(f"=== {tomato.__class__.__name__.capitalize()}")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for day in range(20):
        tomato.age()
        tomato.grow()
        tomato._nutritional_value += 1
    tomato.show()


if __name__ == "__main__":
    main()
