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

    def output(self) -> tuple[int, str]:
        self._extracted_count += 1
        return self._extracted_count, self._data.pop(0)


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if proc not in self._processors:
            self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        """Analyzes each element and polymorphically routes it to an appropriate processor."""
        for item in stream:
            routed = False
            for processor in self._processors:
                if processor.validate(item):
                    processor.ingest(item)
                    routed = True
                    break  # Element handled, move to the next item in the stream

            if not routed:
                print(
                    f"[ERROR] No registered processor can handle element: {item} (Type: {type(item).__name__})")

    def print_processors_stats(self) -> None:
        """Prints current stream and ingestion queue statistics for each processor."""
        print("\n--- Processors Statistics ---")
        for proc in self._processors:
            name = proc.__class__.__name__
            print(
                f" * {name}: Items in queue = {proc.queue_size}, Total extracted so far = {proc._extracted_count}")
        print("-----------------------------\n")


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
        if (isinstance(data, str) or isinstance(data, list) and
                all(isinstance(x, str) for x in data)):
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("Improper text data")
        if isinstance(data, list):
            self._data.extend(
                data)  # because they want as separate strings
        else:
            self._data.append(data)


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(isinstance(k, str) and isinstance(v, str) for k, v in
                       data.items())
        if isinstance(data, list):
            return all(
                isinstance(item, dict) and all(
                    isinstance(k, str) and isinstance(v, str) for k, v in
                    item.items())
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


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")


if __name__ == "__main__":
    main()
