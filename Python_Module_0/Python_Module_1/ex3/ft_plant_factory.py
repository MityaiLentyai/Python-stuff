#!/usr/bin/env python3


class Plant:

    def __init__(self, name: str, height: float, age_days: int):
        self.name: str = name
        self.height: float = height
        self.age_days: int = age_days

    def show(self) -> None:
        print(f"{self.name}: height={self.height}, age_days={self.age_days}")


def main() -> None:
    print("=== Plant Factory Output ===")
    garden: list[Plant] = [
        Plant("Rose", 25.0, 30),
        Plant("Bamboo", 80.0, 10),
        Plant("Cactus", 10.0, 100),
        Plant("Sunflower", 40.0, 45),
        Plant("Cactus", 15.0, 120),
    ]

    for plant in garden:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
