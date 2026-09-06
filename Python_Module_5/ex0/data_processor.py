from abc import ABC, abstractmethod
from collections.abc import Sequence
import typing


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._data: list[str] = []
        self._extracted_count: int = 0

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str] | None:
        if not self._data:
            return None
        self._extracted_count += 1
        return self._extracted_count, self._data.pop(0)


class NumericProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(
                isinstance(item, (int, float)) and not isinstance(item, bool)
                for item in data
            )
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._data.append(str(item))
        else:
            self._data.append(str(data))


class TextProcessor(DataProcessor):

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: str | list[str]) -> None:
        pass


class LogProcessor(DataProcessor):

    @abstractmethod
    def validate(self, data: str) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass


def main():
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    numeric_processor = NumericProcessor()
    print(f" Trying to validate input '42':"
          f"{numeric_processor.validate(42)}")
    print(f" Trying to validate input 'Hello'"
          f":{numeric_processor.validate('Hello')}")
    print(f" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric_processor.ingest('foo')
    except TypeError as e:
        print(" Got exception:", e)
    test_list = [1, 2, 3, 4, 5]
    print(f" Processing data: {test_list}")
    numeric_processor.ingest(test_list)
    print(" Extracting 3 values:...")
    for i in range(3):
        print(f" Numeric value {i}: {numeric_processor.output()[0]}")

    print("\nTesting Text Processor...")


if __name__ == "__main__":
    main()
