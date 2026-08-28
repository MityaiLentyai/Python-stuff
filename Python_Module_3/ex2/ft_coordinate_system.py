import math


def game():
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")

    while(True):
        # fmt: off
        try:
            user_input = input(
                "Enter new coordinates Enter new"
                "coordinates as floats in format 'x,y,z': "
            ).split(',')
            coords = tuple(float(value) for value in user_input)
            print(coords)
        except Exception:
            print("Invalid syntax")
        # fmt: on


game()
