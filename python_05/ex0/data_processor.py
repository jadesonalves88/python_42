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


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    print("Testing Numeric Processor...")
    np = NumericProcessor()
    print(f"Trying to validate input '42': {np.validate(42)}")
    print(f"Trying to validate input 'Hello': {np.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np.ingest("foo")  # type: ignore
    except TypeError as e:
        print(f"Got exception: {e}")
    print("Processing data: [1, 2, 3, 4, 5]")
    np.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for _i in range(3):
        rank, val = np.output()
        print(f"Numeric value {rank}: {val}")

    print("Testing Text Processor...")
    tp = TextProcessor()
    print(f"Trying to validate input '42': {tp.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    tp.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    rank, val = tp.output()
    print(f"Text value {rank}: {val}")

    print("Testing Log Processor...")
    lp = LogProcessor()
    print(f"Trying to validate input 'Hello': {lp.validate('Hello')}")
    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {log_data}")
    lp.ingest(log_data)
    print("Extracting 2 values...")
    for _i in range(2):
        rank, val = lp.output()
        print(f"Log entry {rank}: {val}")
