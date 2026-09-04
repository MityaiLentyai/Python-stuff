import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return None

    print("=== Cyber Archives Recovery & Preservation ===")
    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")

    content: str = ""

    try:
        file: typing.IO[str] = open(file_name, "r")
        print("---\n")
        content = file.read()
        print(content)
        print("\n---")
        file.close()
        print(f"File '{file_name}' closed.")
    except FileNotFoundError as e:
        print(
              f"[STDERR] Error opening file '{file_name}': {e}",
              file=sys.stderr
        )
        return None
    except PermissionError as e:
        print(
              f"[STDERR] Error opening file '{file_name}': {e}",
              file=sys.stderr
        )
        return None

    print("\nTransform data:")
    print("---\n")

    lines = content.splitlines()
    transformed_content = "\n".join([f"{line}#" for line in lines])
    if content.endswith("\n") and transformed_content:
        transformed_content += "\n"

    print(transformed_content)
    print("\n---\n")

    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()

    raw_input = sys.stdin.readline()

    if raw_input.endswith("\n"):
        new_file_name = raw_input[:-1]
    else:
        new_file_name = raw_input

    if not new_file_name:
        print("Not saving data.")
        return None
    else:
        print(f"Saving data to '{new_file_name}'")
        try:
            new_file_object: typing.IO[str] = open(new_file_name, "w")
            new_file_object.write(transformed_content)
            new_file_object.close()
            print(f"Data saved in '{new_file_name}'")
        except FileNotFoundError as e:
            print(
                  f"[STDERR] Error opening file '{new_file_name}':{e}",
                  file=sys.stderr
            )
            print("Data not saved.")
        except PermissionError as e:
            print(
                f"[STDERR] Error opening file '{new_file_name}': {e}",
                file=sys.stderr
            )
            print("Data not saved.")


if __name__ == "__main__":
    main()
