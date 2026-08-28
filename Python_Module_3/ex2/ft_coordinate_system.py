import math


def game():
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")

    while True:
        # fmt: off
        try:
            user_input = input(
                "Enter new coordinates Enter new"
                "coordinates as floats in format 'x,y,z': "
            ).split(',')
            x, y, z = tuple(float(value) for value in user_input)
            print(x, y, z)
            print("It includes: ", end="")
            print(f"X={x}", )
            print(f"Y={y}")
            print(f"Z={z}")
            return x, y, z

            break
        except Exception:
            print("Invalid syntax")
        # fmt: on



game()
