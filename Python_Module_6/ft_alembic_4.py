import alchemy

print("=== Alembic 4 ===\n"
      "Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air:"
      f" {alchemy.create_air()}")  # type: ignore[attr-defined]
print("Now show that not all functions can be reached")
print("This will raise an exception!")
try:
    print(f"{alchemy.create_earth()}")  # type: ignore[attr-defined]
except AttributeError:
    print("Error, I am dead now, I leave all that I own to my cat Guppy")
