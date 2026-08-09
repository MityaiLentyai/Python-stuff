#!/usr/bin/env python3

class Plant:

    all_plants: list["Plant"] = []

    def __init__(self, name,  height,  age):
        self.name = name
        self.height = height
        self.age = age

        Plant.all_plants.append(self)

    @classmethod
    def show(cls):
        print("=== Garden Plant Registry ===")
        if not Plant.all_plants:
            print("No plants received yet")
            return

        for plant in cls.all_plants:
            print(f"{plant.name.capitalize()}: {plant.height}cm, "
                  f"{plant.age} days old")


def main():

    Plant("rose", 25, 30)
    Plant("sunflower", 80, 45)
    Plant("cactus", 15, 120)
    Plant.show()


if __name__ == "__main__":
    main()
