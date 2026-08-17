#!/usr/bin/env python3


class Plant:

    def __init__(self, _name: str, _height: float, _age_days: int):
        self._name: str = _name
        self._height: float = _height
        self._age_days: int = _age_days

    # fmt: off
    def show(self) -> None:
        print(f"{self._name.capitalize()}: {self._height}cm, "
              f"{self._age_days} days old")
    # fmt: on

    def set_height(self, new_height: float) -> None:
        if new_height > 0:
            self._height = new_height
            print(f"Height updated: {int(self._height)}cm")
        else:
            print(f"{self._name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, new_age: int) -> None:
        if new_age > 0:
            self._age_days = new_age
            print(f"Age updated: {self._age_days} days")
        else:
            print(f"{self._name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25.0)
    rose.set_age(30)
    print()
    rose.set_height(-2)
    rose.set_age(-2)
    print()
    # fmt: off
    print(f"Current state: {rose._name.capitalize()}: {rose.get_height()}cm, "
          f"{rose.get_age()} days old")
    # fmt: on


if __name__ == "__main__":
    main()
