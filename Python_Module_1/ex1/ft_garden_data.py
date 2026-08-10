#!/usr/bin/env python3

class Plant:

    def __init__(self, name,  height,  age):
        self.name = name
        self.height = height
        self.age = age

    def show(plant):
        print("=== Garden Plant Registry ===")
        if not plant:
            print("No plants received yet")
            return

        print(f"{plant.name.capitalize()}: {plant.height}cm, "
              f"{plant.age} days old")


def main():

    rose = Plant("rose", 25, 30)
    sunflower = Plant("sunflower", 80, 45)
    cactus = Plant("cactus", 15, 120)
    Plant.show(rose)
    Plant.show(sunflower)
    Plant.show(cactus)


if __name__ == "__main__":
    main()
