from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._counter: int = 0
        self.total_ingested: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        return self._data.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list) and data:
            return all(
                isinstance(x, (int, float)) and not isinstance(x, bool)
                for x in data
            )
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")
        items: list[int | float]
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        for item in items:
            self._data.append((self._counter, str(item)))
            self._counter += 1
            self.total_ingested += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and data:
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("Improper text data")
        items: list[str]
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        for item in items:
            self._data.append((self._counter, item))
            self._counter += 1
            self.total_ingested += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            if not data:
                return False
            return (
                all(isinstance(k, str) and isinstance(v, str)
                    for k, v in data.items())
                and "log_level" in data
                and "log_message" in data
            )
        if isinstance(data, list) and data:
            return all(
                isinstance(item, dict)
                and all(isinstance(k, str) and isinstance(v, str)
                        for k, v in item.items())
                and "log_level" in item
                and "log_message" in item
                for item in data
            )
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")
        items: list[dict[str, str]]
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        for item in items:
            log_str = f"{item['log_level']}: {item['log_message']}"
            self._data.append((self._counter, log_str))
            self._counter += 1
            self.total_ingested += 1


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [val for _, val in data]
        print("CSV Output:")
        print(",".join(values))


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        parts = [f'"item_{rank}": "{val}"' for rank, val in data]
        print("JSON Output:")
        print("{" + ", ".join(parts) + "}")


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            processed = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    processed = True
                    break
            if not processed:
                print(
                    "DataStream error - "
                    f"Can't process element in stream: {element}"
                )

    def output_pipeline(
        self, nb: int, plugin: ExportPlugin
    ) -> None:
        for proc in self._processors:
            data: list[tuple[int, str]] = []
            for _ in range(min(nb, len(proc._data))):
                data.append(proc.output())
            if data:
                plugin.process_output(data)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            name = type(proc).__name__
            total = proc.total_ingested
            remaining = len(proc._data)
            print(
                f"{name}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("Registering Processors")
    ds.register_processor(NumericProcessor())
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO",
             "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {batch}")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVPlugin()
    ds.output_pipeline(3, csv_plugin)
    ds.print_processors_stats()

    batch2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR",
             "log_message": "500 server crash"},
            {"log_level": "NOTICE",
             "log_message": "Certificate expires in 10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"Send another batch of data: {batch2}")
    ds.process_stream(batch2)
    ds.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONPlugin()
    ds.output_pipeline(5, json_plugin)
    ds.print_processors_stats()
