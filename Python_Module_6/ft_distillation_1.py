import alchemy

print("=== Distillation 1 ===")
print("Using: 'import alchemy' structure to access potions")
print(f"Testing strength_potion: {alchemy.strength_potion()}")
print(f"Testing healing_potion: "
      f"{alchemy.heal()}")  # type: ignore[attr-defined]
