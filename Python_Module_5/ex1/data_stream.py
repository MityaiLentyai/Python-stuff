from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._extracted_count: int = 0
        self._total_processed: int = 0
        self._data: list[str] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    @abstractmethod
    def show_stats(self) -> None:
        pass

    @property
    def queue_size(
            self) -> int:
        return len(self._data)

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No items remaining to extract.")
        self._extracted_count += 1
        return self._extracted_count, self._data.pop(0)


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        return (isinstance(data, (int, float))
                or (isinstance(data, list) and
                    all(isinstance(x, (int, float)) and not isinstance(x, bool)
                        for x in data)))

    def ingest(self, data: float | list[float]) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._data.append(str(item))
                self._total_processed += 1
        else:
            self._data.append(str(data))
            self._total_processed += 1

    def show_stats(self) -> None:
        print(
            f"Numeric Processor: total {self._total_processed} items processed"
            f", remaining {self.queue_size} on processor")


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and all(isinstance(x, str) for x in data):
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._data.append(item)
                self._total_processed += 1
        else:
            self._data.append(data)
            self._total_processed += 1

    def show_stats(self) -> None:
        print(
            f"Text Processor: total {self._total_processed} items processed,"
            f" remaining {self.queue_size} on processor")


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return "log_level" in data and "log_message" in data
        if isinstance(data, list):
            return (len(data) > 0
                    and all(isinstance(item, dict)
                            and "log_level" in item
                            and "log_message" in item
                            for item in data
                            ))
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")
        if isinstance(data, list):
            for dct in data:
                self._data.append(f"{dct['log_level']}: {dct['log_message']}")
                self._total_processed += 1
        else:
            self._data.append(f"{data['log_level']}: {data['log_message']}")
            self._total_processed += 1

    def show_stats(self) -> None:
        print(
            f"Log Processor: total {self._total_processed} items processed,"
            f" remaining {self.queue_size} on processor")


class DataStream:

    def __init__(self, name: str) -> None:
        self.name: str = name
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if proc not in self._processors:
            self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            routed = False
            for processor in self._processors:
                if processor.validate(item):
                    processor.ingest(item)
                    routed = True
                    break
            if not routed:
                print(
                    f"DataStream error - "
                    f"Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:
            name_map = {
                "NumericProcessor": "Numeric Processor",
                "TextProcessor": "Text Processor",
                "LogProcessor": "Log Processor"
            }
            display_name = name_map.get(proc.__class__.__name__,
                                        proc.__class__.__name__)
            print(
                f"{display_name}: total {proc._total_processed} items "
                f"processed, remaining {proc.queue_size} on processor"
            )


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    data_stream = DataStream("test_stream")
    data_stream.print_processors_stats()
    print()

    print("Registering Numeric Processor\n")
    numeric_proc = NumericProcessor()
    data_stream.register_processor(numeric_proc)

    test_data = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil isconnected'}],
        42,
        ['Hi', 'five']
    ]

    print("Send first batch of data on stream:", test_data)
    data_stream.process_stream(test_data)
    data_stream.print_processors_stats()
    print()

    print("Registering other data processors")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    data_stream.register_processor(text_proc)
    data_stream.register_processor(log_proc)

    print("Send the same batch again")
    data_stream.process_stream(test_data)
    data_stream.print_processors_stats()
    print()

    print(
        "Consume some elements from the data processors:"
        " Numeric 3, Text 2, Log 1")
    for _ in range(3):
        numeric_proc.output()
    for _ in range(2):
        text_proc.output()
    log_proc.output()

    data_stream.print_processors_stats()
