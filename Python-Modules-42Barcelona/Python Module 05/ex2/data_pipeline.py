from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Protocol
import json


class DataProcessor(ABC):
    """Abstract base class defining the common processing interface."""

    def __init__(self):
        self._data: List[str] = []
        self._rank: int = 0
        self.processed_count: int = 0
        self.name: str = "Data Processor"

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

    def __init__(self):
        super().__init__()
        self.name = "Numeric Processor"

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
            self.processed_count += len(data)
            for item in data:
                self._data.append(str(item))
        else:
            self.processed_count += 1
            self._data.append(str(data))


class TextProcessor(DataProcessor):
    """Processor specialized for text data."""

    def __init__(self):
        super().__init__()
        self.name = "Text Processor"

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
            self.processed_count += len(data)
            self._data.extend(data)
        else:
            self.processed_count += 1
            self._data.append(data)


class LogProcessor(DataProcessor):
    """Processor specialized for log data."""

    def __init__(self):
        super().__init__()
        self.name = "Log Processor"

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
            self.processed_count += len(data)
            for item in data:
                level = item.get('log_level', 'UNKNOWN')
                message = item.get('log_message', '')
                self._data.append(f"{level}: {message}")
        else:
            self.processed_count += 1
            level = data.get('log_level', 'UNKNOWN')
            message = data.get('log_message', '')
            self._data.append(f"{level}: {message}")


class ExportPlugin(Protocol):
    """Protocol for export plugins."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """Process the output data."""
        ...


class CSVExportPlugin:
    """CSV export plugin."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """Output data as CSV."""
        values = [value for rank, value in data]
        line = ",".join(values)
        print(f"CSV Output:")
        print(line)


class JSONExportPlugin:
    """JSON export plugin."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """Output data as JSON."""
        output_dict = {f"item_{rank}": value for rank, value in data}
        json_str = json.dumps(output_dict)
        print(f"JSON Output:")
        print(json_str)


class DataStream:
    """Handles routing data to appropriate processors."""

    def __init__(self):
        self.processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        """Register a new data processor."""
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        """Process each element in the stream by routing to appropriate processor."""
        for item in stream:
            processed = False
            for proc in self.processors:
                if proc.validate(item):
                    proc.ingest(item)
                    processed = True
                    break
            if not processed:
                print(f"DataStream error - Can't process element in stream: {item!r}")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """Consume nb elements from each processor and export using plugin."""
        for proc in self.processors:
            data = []
            for _ in range(min(nb, len(proc._data))):
                data.append(proc.output())
            if data:
                plugin.process_output(data)

    def print_processors_stats(self) -> None:
        """Print statistics of all registered processors."""
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            print(f"{proc.name}: total {proc.processed_count} items processed, remaining {len(proc._data)} on processor")


def main() -> None:
    """Entry point: test the data pipeline."""
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("Registering Processors")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)

    batch = ['Hello world', [3.14, -1, 2.71], [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, {'log_level': 'INFO', 'log_message': 'User wil is connected'}], 42, ['Hi', 'five']]
    print(f"Send first batch of data on stream: {batch!r}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    stream.output_pipeline(3, csv_plugin)
    stream.print_processors_stats()

    batch2 = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'], [{'log_level': 'ERROR', 'log_message': '500 server crash'}, {'log_level': 'NOTICE', 'log_message': 'Certificate expires in 10 days'}], [32, 42, 64, 84, 128, 168], 'World hello']
    print(f"Send another batch of data: {batch2!r}")
    stream.process_stream(batch2)
    stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    stream.output_pipeline(5, json_plugin)
    stream.print_processors_stats()


if __name__ == "__main__":
    main()