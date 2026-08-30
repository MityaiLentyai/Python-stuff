import sys

args_dict = {}

for arg in sys.argv[1:]:
    if ":" not in arg:
        print(f"Invalid parameter '{arg}'")
        continue

    # Split into key and value
    key, val = arg.split(":", 1)

    try:
        args_dict[key] = int(val)
    except ValueError as e:
        print(f"Quantity error for '{key}': {e}")

print("\nGot inventory:", args_dict)
