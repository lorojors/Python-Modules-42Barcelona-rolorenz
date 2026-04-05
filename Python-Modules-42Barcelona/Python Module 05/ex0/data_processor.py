from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union


class DataProcessor(ABC):
    """Abstract base class defining the common processing interface."""

    def __init__(self):
        self._data: List[str] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Ingest the data."""
        pass

    def output(self) -> tuple[int, str]:
        """Extract the oldest piece of data with its rank."""
        if not self._data:
            raise IndexError("No data to output")
        value = self._data.pop(0)
        rank = self._rank
        self._rank += 1
        return rank, value


class NumericProcessor(DataProcessor):
    """Processor specialized for numeric data."""

    def validate(self, data: Any) -> bool:
        """Return True if data is int, float, or list of int/float."""
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return False

    def ingest(self, data: Union[int, float, List[Union[int, float]]]) -> None:
        """Ingest numeric data."""
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._data.append(str(item))
        else:
            self._data.append(str(data))


class TextProcessor(DataProcessor):
    """Processor specialized for text data."""

    def validate(self, data: Any) -> bool:
        """Return True if data is str or list of str."""
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: Union[str, List[str]]) -> None:
        """Ingest text data."""
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._data.append(item)
        else:
            self._data.append(data)


class LogProcessor(DataProcessor):
    """Processor specialized for log data."""

    def validate(self, data: Any) -> bool:
        """Return True if data is dict[str, str] or list of such."""
        if isinstance(data, dict):
            return all(isinstance(k, str) and isinstance(v, str) for k, v in data.items())
        if isinstance(data, list):
            return all(
                isinstance(item, dict) and all(isinstance(k, str) and isinstance(v, str) for k, v in item.items())
                for item in data
            )
        return False

    def ingest(self, data: Union[Dict[str, str], List[Dict[str, str]]]) -> None:
        """Ingest log data."""
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for item in data:
                level = item.get('log_level', 'UNKNOWN')
                message = item.get('log_message', '')
                self._data.append(f"{level}: {message}")
        else:
            level = data.get('log_level', 'UNKNOWN')
            message = data.get('log_message', '')
            self._data.append(f"{level}: {message}")


def main() -> None:
    """Entry point: test the architecture."""
    print("=== Code Nexus - Data Processor ===")

    # Create instances
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    # Test Numeric Processor
    print("Testing Numeric Processor...")
    print(f"Trying to validate input {42!r}: {numeric.validate(42)}")
    print(f"Trying to validate input {'Hello'!r}: {numeric.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest('foo')
    except ValueError as exc:
        print(f"Got exception: {exc}")
    print("Processing data: [1, 2, 3, 4, 5]")
    numeric.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = numeric.output()
        print(f"Numeric value {rank}: {value}")

    # Test Text Processor
    print("Testing Text Processor...")
    print(f"Trying to validate input {42!r}: {text.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text.ingest(['Hello', 'Nexus', 'World'])
    print("Extracting 1 value...")
    rank, value = text.output()
    print(f"Text value {rank}: {value}")

    # Test Log Processor
    print("Testing Log Processor...")
    print(f"Trying to validate input {'Hello'!r}: {log.validate('Hello')}")
    data = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f"Processing data: {data!r}")
    log.ingest(data)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print(f"Log entry {rank}: {value}")


if __name__ == "__main__":
    main()