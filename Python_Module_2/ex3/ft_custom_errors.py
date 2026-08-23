def test_errors() -> None:
    pass


class GardenError(Exception):
    pass


class PlantError(GardenError):

    def error_message():
        print("The tomato plant is wilting!")


class WaterError(GardenError):
    pass


print("=== Custom Garden Errors Demo ===")
raise (GardenError)
