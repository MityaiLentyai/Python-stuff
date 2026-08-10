#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str,  height: float,  age_days: int):
        self.name: str = name
        self.height: float = height
        self.age_days: int = age_days

    def age(self):
        self.age_days += 1

    def grow(self):
        self.height = round(self.height * 1.01, 1)
    def show(self):
        if not self:
            print("No plants received yet")
            return

        print(f"{self.name.capitalize()}: {self.height}cm, "
              f"{self.age_days} days old")


def main() -> None:
    print("=== Plant Factory Output ===")
    garden: list[Plant] = [
        Plant("Rose", 25.0, 30),
        Plant("Bamboo", 50.0, 10),
        Plant("Cactus", 10.0, 100)
    ]

    for plant in garden:
        plant.show()

if __name__ == "__main__":
    main()
