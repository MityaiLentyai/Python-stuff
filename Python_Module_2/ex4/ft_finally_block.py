class Plant:

    def __init__(self, name: str) -> None:
        self.name = name


class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Caught PlantError:"):
        super().__init__(message)


def water_plant(plant: str) -> None:
    if plant == plant.capitalize():
        print(f"Watering {plant}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant}'")


def test_watering_system() -> None:
    tomato = Plant("Tomato")
    lettuce = Plant("Lettuce")
    carrots = Plant("Carrots")
    invalid_lettuce = Plant("lettuce")

    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant(tomato.name)
        water_plant(lettuce.name)
        water_plant(carrots.name)
    finally:
        print("Closing watering system\n")

    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant(tomato.name)
        water_plant(invalid_lettuce.name)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system\n")
        print("Cleanup always happens, even with errors!")


def main() -> None:
    test_watering_system()


if __name__ == "__main__":
    main()
