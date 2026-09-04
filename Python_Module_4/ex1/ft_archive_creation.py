import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return None

    print("=== Cyber Archives Recovery & Preservation ===")
    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")
    try:
        file = open(file_name, "r")
        print("---\n")
        content = file.read()
        print(content)
        print("---")
        file.close()
        print(f"File '{file_name}' closed.")
    except FileNotFoundError as e:
        print(f"Error opening file '{file_name}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{file_name}': {e}")

    print("Transform data:\n---\n")
    content = content.replace("\n", "#\n")
    print(content)
    print("---")
    new_file_name = input("Enter new file name (or empty):")
    if not new_file_name:
        print("Not saving data.")
        return
    else:
        print(f"Saving data to '{new_file_name}'")
        new_file_object = open(new_file_name, "w")
        new_file_object.write(content)
        print(f"Data saved in '{new_file_name}'")


if __name__ == "__main__":
    main()
