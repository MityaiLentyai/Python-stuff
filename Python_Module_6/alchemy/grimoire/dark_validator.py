from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()

    lower_ingredients = ingredients.casefold()

    for item in allowed:
        if item.casefold() in lower_ingredients:
            return f"Ingredients: {ingredients} -> VALID"

    return f"Ingredients: {ingredients} -> INVALID"
