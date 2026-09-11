from abc import ABC, abstractmethod
from typing import Any, Protocol


class ExportPlugin(Protocol):
    """Protocol enabling a duck-typed plugin system for exporting processing metrics."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    """Manually serializes processor queues into a CSV formatted string."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        print("CSV Output:")
        # Join values with commas as per standard CSV format requirements
        csv_string = ",".join(item[1] for item in data)
        print(csv_string)


class JSONExportPlugin:
    """Manually serializes processor queues into valid JSON strings with structured keys."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        print("JSON Output:")
        # Build valid JSON structure manually by generating incremental "item_X" keys
        kv_pairs = []
        for index, val in data:
            # Escape inner double quotes inside messages to keep JSON strings valid
            escaped_val = val.replace('"', '\\"')
            kv_pairs.append(f'"item_{index}": "{escaped_val}"')

        json_string = "{" + ", ".join(kv_pairs) + "}"
        print(json_string)


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._extracted_count: int = 0
        self._total_processed: int = 0
        self._data: list[str] = []

    @property
    def queue_size(self) -> int:
        return len(self._data)

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No items remaining to extract.")
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
                self._total_processed += 1
        else:
            self._data.append(str(data))
            self._total_processed += 1


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


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return "log_level" in data and "log_message" in data
        if isinstance(data, list):
            return len(data) > 0 and all(
                isinstance(item,
                           dict) and "log_level" in item and "log_message" in item
                for item in data
            )
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
                    f"DataStream error - Can't process element in stream: {item}")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """Consumes up to 'nb' elements from each processor and pushes them to the exporter."""
        for proc in self._processors:
            extracted_items = []
            # Stop safely if the number requested exceeds items in queue
            items_to_take = min(nb, proc.queue_size)
            for _ in range(items_to_take):
                extracted_items.append(proc.output())

            # Send the batch array out to the plugin handler
            if extracted_items:
                plugin.process_output(extracted_items)

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
                f"{display_name}: total {proc._total_processed} items processed, "
                f"remaining {proc.queue_size} on processor")


def main() -> None:
    print("--- Code Nexus - Data Pipeline ---")
    print("\nInitialize Data Stream...\n")
    stream = DataStream("production_pipeline")
    stream.print_processors_stats()

    print("\nRegistering Processors")
    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    stream.register_processor(num_proc)
    stream.register_processor(text_proc)
    stream.register_processor(log_proc)

    # --- BATCH 1 ---
    batch_1 = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]
    print(f"\nSend first batch of data on stream: {batch_1}\n")
    stream.process_stream(batch_1)
    stream.print_processors_stats()

    # --- PIPELINE EXPORT 1 (CSV) ---
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    stream.output_pipeline(3, csv_plugin)
    print()
    stream.print_processors_stats()

    # --- BATCH 2 ---
    batch_2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
         {'log_level': 'NOTICE',
          'log_message': 'Certificate expires in 10 days'}],
    ,
    ['World hello']
    ]
    print(f"\nSend another batch of data: {batch_2}\n")
    stream.process_stream(batch_2)
    stream.print_processors_stats()

    # --- PIPELINE EXPORT 2 (JSON) ---
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    stream.output_pipeline(5, json_plugin)
    print()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
