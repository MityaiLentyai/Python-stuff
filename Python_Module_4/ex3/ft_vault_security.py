def secure_archive(
    file_name: str, action: str = "r", write_content: str = ""
) -> (bool, str):
    try:
        with open(file_name, action) as file:
            if action == "r":
                content = file.read()
                print("(True", repr(content), ")")
                return (True, content)
            if action == "w":
                content = file.write(write_content)
                print("(True, 'Content successfully written to file')")
                return (True, content)

    except FileNotFoundError as e:
        # fmt: off
        print(f"(False, \"{e}\")")
        # fmt: on
    except PermissionError as e:
        # fmt: off
        print(f"('False, \"{e}\")")
        # fmt: on


def main() -> None:
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    secure_archive("Fooo")
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    secure_archive("broken_bitch.txt")
    print("\nUsing 'secure_archive' to read from a regular file:")
    previous_content = secure_archive("regular.txt", "r")
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    secure_archive("new_txt.txt", "w", previous_content[1])


if __name__ == "__main__":
    main()
