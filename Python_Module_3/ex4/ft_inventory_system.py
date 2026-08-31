import sys

print("=== Inventory System Analysis ===")

args_dict = {}

for arg in sys.argv[1:]:
    # Fix 1: Check for the delimiter BEFORE trying to split
    if ":" not in arg:
        print(f"Error - invalid parameter '{arg}'")
        continue

    key, val = arg.split(":", 1)

    # Fix 2: Check for duplicates BEFORE adding to the dictionary
    if key in args_dict:
        print(f"Redundant item '{key}' - discarding")
        continue

    # Fix 3: Validate the integer conversion securely
    try:
        args_dict[key] = int(val)
    except ValueError as e:
        print(f"Quantity error for '{key}': {e}")
        continue  # Skip to the next argument on failure

item_list = list(args_dict.keys())
quantity = sum(args_dict.values())

print("Got inventory:", args_dict)
print("Item list:", item_list)
print(f"Total quantity of the {len(item_list)} items: {quantity}")

for key, value in args_dict.items():
    percentage = round((value / quantity) * 100, 1)
    print(f"Item {key} represents {percentage}%")

max_item = max(args_dict, key=args_dict.get)
min_item = min(args_dict, key=args_dict.get)

max_value = args_dict[max_item]
min_value = args_dict[min_item]

print(f"Item most abundant: {max_item} with quantity {max_value}")
print(f"Item least abundant: {min_item} with quantity {min_value}")

args_dict.update({"magic_item": 1})
print(f"Updated inventory: {args_dict}")
