class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def water_plant(moisture_level: int) -> None:
    if moisture_level < 65:
        raise PlantError("The tomato plant is wilting!")


def tank_level(deduction_level: int, tank_level: int) -> None:
    if tank_level - deduction_level < 0:
        raise WaterError("Not enough water in the tank!")


def test_errors() -> None:
    """
    Maybe it could be done better by lambda functions but I hardcoded it like
    this because I dunno
    """
    try:
        water_plant(60)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        tank_level(5, 3)
    except GardenError as e:
        print(f"Caught GardenError: {e}")


print("=== Custom Garden Errors Demo ===")
print()
print("Testing PlantError...")
try:
    water_plant(55)
except PlantError as e:
    print(f"Caught PlantError: {e}")
print()

print("Testing WaterError...")
try:
    tank_level(5, 3)
except WaterError as e:
    print(f"Caught WaterError: {e}")
print()


print("Testing catching all garden errors...")
test_errors()
print()

print("All custom error types work correctly!")
