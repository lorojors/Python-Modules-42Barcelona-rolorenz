def validate_ingredients(ingredients: str):
    from .light_spellbook import light_spell_allowed_ingredients
    allowed = light_spell_allowed_ingredients()
    ing_lower = ingredients.lower()
    if any(a.lower() in ing_lower for a in allowed):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"