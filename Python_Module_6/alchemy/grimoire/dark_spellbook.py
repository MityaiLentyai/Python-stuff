from .dark_validator import validate_ingredients

def dark_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]

def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validation_status = validate_ingredients(ingredients)

    if "VALID" in validation_status:
        return f"Spell '{spell_name}' has been RECORDED."
    return f"Spell '{spell_name}' was REJECTED due to invalid ingredients"
