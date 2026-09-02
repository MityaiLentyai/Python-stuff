import sys

print("=== Inventory System Analysis ===")

args_dict = {}

for arg in sys.argv[1:]:
    if ":" not in arg:
        print(f"Error - invalid parameter '{arg}'")
        continue

    key, val = arg.split(":", 1)

    if key in args_dict:
        print(f"Redundant item '{key}' - discarding")
        continue

    try:
        args_dict[key] = int(val)
    except ValueError as e:
        print(f"Quantity error for '{key}': {e}")
        continue

item_list = list(args_dict.keys())
quantity = sum(args_dict.values())

print("Got inventory:", args_dict)
print("Item list:", item_list)
print(f"Total quantity of the {len(item_list)} items: {quantity}")

for key, value in args_dict.items():
    percentage = round((value / quantity) * 100, 1)
    print(f"Item {key} represents {percentage}%")

try:
    max_item = None
    max_value = None
    min_item = None
    min_value = None

    for item, count in args_dict.items():
        if max_value is None or count > max_value:
            max_item = item
            max_value = count
        if min_value is None or count < min_value:
            min_item = item
            min_value = count

    print(f"Item most abundant: {max_item} with quantity {max_value}")
    print(f"Item least abundant: {min_item} with quantity {min_value}")
except ValueError:
    print("No correct parameters given, adding the magic item!")

args_dict.update({"magic_item": 1})
print(f"Updated inventory: {args_dict}")
