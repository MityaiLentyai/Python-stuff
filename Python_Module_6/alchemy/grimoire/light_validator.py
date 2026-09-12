from . import light_spellbook

def validate_ingredients(ingredients: str) -> str:
    allowed = light_spellbook.light_spell_allowed_ingredients()

    lower_ingredients = ingredients.casefold()

    for item in allowed:
        if item.casefold() in lower_ingredients:
            return f"({ingredients} -> VALID)"

    return f"({ingredients} -> INVALID)"
