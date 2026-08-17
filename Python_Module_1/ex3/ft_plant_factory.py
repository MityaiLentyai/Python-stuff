#!/usr/bin/env python3

class Plant:

    def __new___(cls, name: str,  height: float,  age_days: int):
        class.name: str = name
        class.height: float = height
        class.age_days: int = age_days

    def __init__()

def main() -> None:
    print("=== Plant Factory Output ===")
    garden: list[Plant] = [
        Plant("Rose", 25.0, 30),
        Plant("Bamboo", 80.0, 10),
        Plant("Cactus", 10.0, 100),
        Plant("Sunflower", 40.0, 45),
        Plant("Cactus", 15.0, 120)
    ]

    for plant in garden:
        plant.show()


if __name__ == "__main__":
    main()
