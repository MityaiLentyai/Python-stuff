class Plant:

    def __init__(self, name):
        self.name = name

def water_plant(plant: str) -> bool:
    if plant == plant.capitalize():
        return True
    else:
        return False


def test_watering_system() -> None:
    tomato = Plant("Tomato")
    carrots = Plant("Carrots")
    sunflower = Plant("Sunflower")
    lettuce = Plant("lettuce")

    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")

    water_plant(tomato.name)
    water_plant(carrots.name)
    water_plant(sunflower.name)
    print("Opening watering system")
    try water_plant():
        pass
    except:
        pass
    finally:
        print("Closing watering system")


class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Caught PlantError:"):
        super().__init__(message)




