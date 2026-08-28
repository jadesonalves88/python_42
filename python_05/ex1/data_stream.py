from abc import ABC, abstractmethod
from typing import Any


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
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("Registering Numeric Processor")
    ds.register_processor(NumericProcessor())

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

    print("Registering other data processors")
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    print("Send the same batch again")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    n_proc = ds._processors[0]
    t_proc = ds._processors[1]
    l_proc = ds._processors[2]
    for _ in range(3):
        n_proc.output()
    for _ in range(2):
        t_proc.output()
    for _ in range(1):
        l_proc.output()
    ds.print_processors_stats()
