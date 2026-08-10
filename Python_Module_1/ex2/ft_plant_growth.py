#!/usr/bin/env python3

class Plant:

    all_plants: list["Plant"] = []

    def __init__(self, name: str,  height: float,  age_days: int):
        self.name: str = name
        self.height: float = height
        self.age_days: int = age_days

    def age(self):
        self.age_days += 1

    def grow(self):
        self.height = round(self.height * 1.01, 1)


def main() -> None:
    rose = Plant("rose", 25.0, 30)
    days: int = 1
    print("=== Garden Plant Growth ===")
    print(f"{rose.name.capitalize()}: {rose.height}cm, "
          f"{rose.age_days} days old")

    while days < 8:
        print(f"=== Day {days} ===")
        rose.age()
        rose.grow()
        print(f"{rose.name.capitalize()}: {rose.height}cm, "
              f"{rose.age_days} days old")
        days += 1


if __name__ == "__main__":
    main()
