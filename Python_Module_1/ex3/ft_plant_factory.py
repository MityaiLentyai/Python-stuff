#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: float, age_days: int):
        self.name: str = name
        if not self.name:
            print("No plants received yet")
            return
        self.height: float = height
        if height <= 0:
            print("Height can not be zero or negative")
        self.age_days: int = age_days
        if age_days <= 0:
            print("Age can not be zero or negative")

    def set_height(self, new_hight: int):
        if self.age < 0:
            print(f"{self.name}: Error, can't be negative")
        else:
            self.height = new_hight
            print(f"Height updated: {}")

    def show(self) -> None:
        print(f"{self.name}: height={self.height}, age_days={self.age_days}")


def main() -> None:
    print("=== Plant Factory Output ===")

    rose = Plant("Rose", 15.0, 30)
    print("Plant created: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
