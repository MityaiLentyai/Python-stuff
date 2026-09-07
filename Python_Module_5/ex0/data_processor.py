from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._extracted_count: int = 0
        self._data: list[str] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str] | None:
        if not self._data:
            return None
        self._extracted_count += 1
        return self._extracted_count, self._data.pop(0)


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
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

    def validate(self, data: Any) -> bool:
        if isinstance(data, str) or isinstance(data, list) and all(isinstance(x, str) for x in data):
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("Improper text data")
        if isinstance(data, list):
            self._data.extend(data) #because they want as separate strings/could be done with for
        else:
            self._data.append(data)


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(isinstance(k, str) and isinstance(v, str) for k, v in data.items())
        if isinstance(data, list):
            return all(
                isinstance(item, dict) and all(isinstance(k, str) and isinstance(v, str) for k, v in item.items())
                for item in data
            )
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")
        else:
            if isinstance(data, list):
                for dct in data:
                    self._data.append(
                        f"{dct['log_level']}: {dct['log_message']}")
            else:
                self._data.append(
                    f"{data['log_level']}: {data['log_message']}")

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
    text_processor = TextProcessor()
    print(f" Trying to validate input '42': {text_processor.validate(42)}")
    test_list = ["Hello","Nexus","World"]
    print(f" Processing data: {test_list}")
    text_processor.ingest(test_list)
    print(f" Extracting 1 value... \n"
          f" Text value 0: {text_processor.output()[1]}")

    print("\nTesting Log Processor...")
    log_processor = LogProcessor()
    print(f" Trying to validate input 'Hello': {log_processor.validate('Hello')}")
    test_list = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
                 {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    print(" Extracting 2 values...")
    log_processor.ingest(test_list)
    for i in range(2):
        print(f" Log entry {i}: {log_processor.output()}")

if __name__ == "__main__":
    main()
