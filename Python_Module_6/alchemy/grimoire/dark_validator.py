from . import dark_spellbook

def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spellbook.dark_spell_allowed_ingredients()

    lower_ingredients = ingredients.casefold()

    for item in allowed:
        if item.casefold() in lower_ingredients:
            return f"Ingredients: {ingredients} -> VALID"

    return f"Ingredients: {ingredients} -> INVALID"
