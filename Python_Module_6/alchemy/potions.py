from .elements import create_earth, create_air
from elements import create_water, create_fire


def healing_potion() -> str:
    return (f"Healing potion brewed with"
            f" ’{create_earth()}’ and ’{create_air()}'")


def strength_potion():
    return (f"Strength potion brewed"
            f" with ’{create_fire()}’ and"
            f" ’{create_water()}'")
