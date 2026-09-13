from alchemy import heal, strength_potion


print("=== Distillation 1 ===")
print("Using: 'import alchemy' structure to access potions")
print(f"Testing strength_potion: {strength_potion()}")
print(f"Testing healing_potion: "
      f"{heal()}")  # type: ignore[attr-defined]
