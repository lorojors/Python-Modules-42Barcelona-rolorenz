from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):
    """Abstract base class defining the common processing interface."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return a result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""
        pass

    def format_output(self, result: str) -> str:
        """Format the output string. Can be overridden by subclasses."""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Processor specialized for numeric data (lists of numbers)."""

    def process(self, data: Any) -> str:
        """Process a list of numbers, computing count, sum and average."""
        if not self.validate(data):
            raise ValueError("Invalid data for NumericProcessor.")
        count: int = len(data)
        total: Union[int, float] = sum(data)
        avg: float = total / count
        return f"Processed {count} numeric values, sum={total}, avg={avg}"

    def validate(self, data: Any) -> bool:
        """Return True if data is a non-empty list of numbers."""
        if not isinstance(data, list) or len(data) == 0:
            return False
        return all(isinstance(item, (int, float)) for item in data)

    def format_output(self, result: str) -> str:
        """Format numeric output with Validation header."""
        return (
            "Validation: Numeric data verified\n"
            f"Output: {result}"
        )


class TextProcessor(DataProcessor):
    """Processor specialized for plain text strings."""

    def process(self, data: Any) -> str:
        """Process a string, computing character and word counts."""
        if not self.validate(data):
            raise ValueError("Invalid data for TextProcessor.")
        chars: int = len(data)
        words: int = len(data.split())
        return f"Processed text: {chars} characters, {words} words"

    def validate(self, data: Any) -> bool:
        """Return True if data is a non-empty string."""
        return isinstance(data, str) and len(data.strip()) > 0

    def format_output(self, result: str) -> str:
        """Format text output with Validation header."""
        return (
            "Validation: Text data verified\n"
            f"Output: {result}"
        )


class LogProcessor(DataProcessor):
    """Processor specialized for log-entry strings."""

    # Recognised severity levels in priority order
    LEVELS: List[str] = ["ERROR", "WARNING", "INFO", "DEBUG"]

    def process(self, data: Any) -> str:
        """Parse the log level and message from a log entry string."""
        if not self.validate(data):
            raise ValueError("Invalid data for LogProcessor.")
        level: str = "UNKNOWN"
        message: str = data
        for lvl in self.LEVELS:
            prefix: str = f"{lvl}:"
            if data.startswith(prefix):
                level = lvl
                message = data[len(prefix):].strip()
                break
        return f"[{level}] {level} level detected: {message}"

    def validate(self, data: Any) -> bool:
        """Return True if data is a non-empty string."""
        return isinstance(data, str) and len(data.strip()) > 0

    def format_output(self, result: str) -> str:
        """Format log output with Validation header."""
        return (
            "Validation: Log entry verified\n"
            f"Output: {result}"
        )


def run_individual_demos(
    processors: Dict[str, DataProcessor],
    samples: Dict[str, Any],
    labels: Dict[str, str],
) -> None:
    """Run the labelled individual-processor demonstrations."""
    for key, processor in processors.items():
        print(f"Initializing {labels[key]}...")
        print(f"Processing data: {samples[key]!r}")
        try:
            result: str = processor.process(samples[key])
            print(processor.format_output(result))
        except ValueError as exc:
            print(f"Error: {exc}")
        print()


def run_polymorphic_demo(
    processor_list: List[DataProcessor],
    data_list: List[Any],
) -> None:
    """Process mixed data types through the common interface."""
    print("=== Polymorphic Processing Demo ===")
    print(
        "Processing multiple data types through same interface..."
    )
    results: List[str] = []
    for processor, data in zip(processor_list, data_list):
        try:
            results.append(processor.process(data))
        except ValueError as exc:
            results.append(f"Error: {exc}")

    for idx, result in enumerate(results, start=1):
        print(f"Result {idx}: {result}")
    print()


def main() -> None:
    """Entry point: wire up processors and drive all demonstrations."""
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()

    # ------------------------------------------------------------------ #
    # Processor instances (no constructor parameters required)            #
    # ------------------------------------------------------------------ #
    numeric: NumericProcessor = NumericProcessor()
    text: TextProcessor = TextProcessor()
    log: LogProcessor = LogProcessor()

    # Individual demo configuration
    processors: Dict[str, DataProcessor] = {
        "numeric": numeric,
        "text": text,
        "log": log,
    }
    samples: Dict[str, Any] = {
        "numeric": [1, 2, 3, 4, 5],
        "text": "Hello Nexus World",
        "log": "ERROR: Connection timeout",
    }
    labels: Dict[str, str] = {
        "numeric": "Numeric Processor",
        "text": "Text Processor",
        "log": "Log Processor",
    }

    run_individual_demos(processors, samples, labels)

    # ------------------------------------------------------------------ #
    # Polymorphic demo — same interface, different specialised behaviour  #
    # ------------------------------------------------------------------ #
    poly_processors: List[DataProcessor] = [numeric, text, log]
    poly_data: List[Any] = [
        [1, 2, 3],
        "Hello Nexus",
        "INFO: System ready",
    ]
    run_polymorphic_demo(poly_processors, poly_data)

    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()