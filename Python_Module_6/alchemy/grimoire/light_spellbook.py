def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]

def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    validation_status = validate_ingredients(ingredients)

    if "VALID" in validation_status:
        return f"Spell recorded: {spell_name} {validation_status}."
    return f"Spell '{spell_name}' was REJECTED due to invalid ingredients"
