from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


# ---------------------------------------------------------------------------
# Custom Exceptions
# ---------------------------------------------------------------------------

class StreamError(Exception):
    """Raised when a stream encounters a processing failure."""

    def __init__(self, message: str, stream_id: str) -> None:
        super().__init__(message)
        self.stream_id: str = stream_id


# ---------------------------------------------------------------------------
# Abstract Base Class
# ---------------------------------------------------------------------------

class DataStream(ABC):
    """Abstract base class defining the core streaming interface."""

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.processed_count: int = 0
        self.batch_count: int = 0
        self.stream_type: str = "Generic Stream"

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data and return a result string."""
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """Filter data based on optional criteria string.

        Default implementation returns the full batch unchanged.
        Subclasses override this to apply domain-specific filtering.
        """
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return base stream statistics."""
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "processed_count": self.processed_count,
            "batch_count": self.batch_count,
        }


# ---------------------------------------------------------------------------
# Specialized Stream: SensorStream
# ---------------------------------------------------------------------------

class SensorStream(DataStream):
    """Stream handler specialised for environmental sensor readings."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "Environmental Data"
        self.temp_readings: List[float] = []

    def process_batch(self, data_batch: List[Any]) -> str:
        """Parse sensor tokens and compute average temperature."""
        if not isinstance(data_batch, list) or len(data_batch) == 0:
            raise StreamError(
                "Empty or invalid sensor batch.", self.stream_id
            )
        temps: List[float] = []
        for item in data_batch:
            token: str = str(item)
            if token.startswith("temp:"):
                try:
                    temps.append(float(token.split(":")[1]))
                except ValueError:
                    pass
        self.processed_count += len(data_batch)
        self.batch_count += 1
        self.temp_readings.extend(temps)
        count: int = len(data_batch)
        if temps:
            avg_temp: float = sum(temps) / len(temps)
            return (
                f"Sensor analysis: {count} readings processed, "
                f"avg temp: {avg_temp}°C"
            )
        return f"Sensor analysis: {count} readings processed"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """Filter sensor readings; 'critical' keeps only high temps."""
        if criteria == "critical":
            return [
                item for item in data_batch
                if isinstance(item, str)
                and item.startswith("temp:")
                and float(item.split(":")[1]) > 30.0
            ]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Extend base stats with average temperature."""
        stats: Dict[str, Union[str, int, float]] = super().get_stats()
        if self.temp_readings:
            stats["avg_temp"] = round(
                sum(self.temp_readings) / len(self.temp_readings), 2
            )
        return stats


# ---------------------------------------------------------------------------
# Specialized Stream: TransactionStream
# ---------------------------------------------------------------------------

class TransactionStream(DataStream):
    """Stream handler specialised for financial transaction data."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "Financial Data"
        self.net_flow: float = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Parse buy/sell tokens and compute net flow."""
        if not isinstance(data_batch, list) or len(data_batch) == 0:
            raise StreamError(
                "Empty or invalid transaction batch.", self.stream_id
            )
        net: float = 0.0
        for item in data_batch:
            token: str = str(item)
            if ":" in token:
                direction, _, value_str = token.partition(":")
                try:
                    value: float = float(value_str)
                    net += value if direction == "buy" else -value
                except ValueError:
                    pass
        self.processed_count += len(data_batch)
        self.batch_count += 1
        self.net_flow += net
        sign: str = "+" if net >= 0 else ""
        return (
            f"Transaction analysis: {len(data_batch)} operations, "
            f"net flow: {sign}{int(net)} units"
        )

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """Filter transactions; 'large' keeps values above 100."""
        if criteria == "large":
            filtered: List[Any] = []
            for item in data_batch:
                token: str = str(item)
                if ":" in token:
                    try:
                        value: float = float(token.split(":")[1])
                        if value > 100:
                            filtered.append(item)
                    except ValueError:
                        pass
            return filtered
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Extend base stats with cumulative net flow."""
        stats: Dict[str, Union[str, int, float]] = super().get_stats()
        stats["net_flow"] = self.net_flow
        return stats


# ---------------------------------------------------------------------------
# Specialized Stream: EventStream
# ---------------------------------------------------------------------------

class EventStream(DataStream):
    """Stream handler specialised for system event log entries."""

    ERROR_KEYWORDS: List[str] = ["error", "fail", "critical", "alert"]

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "System Events"
        self.error_count: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Count events and detect error-level entries."""
        if not isinstance(data_batch, list) or len(data_batch) == 0:
            raise StreamError(
                "Empty or invalid event batch.", self.stream_id
            )
        errors: int = sum(
            1 for item in data_batch
            if any(
                kw in str(item).lower()
                for kw in self.ERROR_KEYWORDS
            )
        )
        self.processed_count += len(data_batch)
        self.batch_count += 1
        self.error_count += errors
        return (
            f"Event analysis: {len(data_batch)} events, "
            f"{errors} error detected"
        )

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """Filter events; 'critical' keeps only error-level entries."""
        if criteria == "critical":
            return [
                item for item in data_batch
                if any(
                    kw in str(item).lower()
                    for kw in self.ERROR_KEYWORDS
                )
            ]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Extend base stats with total error count."""
        stats: Dict[str, Union[str, int, float]] = super().get_stats()
        stats["error_count"] = self.error_count
        return stats


# ---------------------------------------------------------------------------
# Stream Manager
# ---------------------------------------------------------------------------

class StreamProcessor:
    """Handles multiple DataStream types polymorphically."""

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def register(self, stream: DataStream) -> None:
        """Register a stream for managed processing."""
        self.streams.append(stream)

    def process_all(
        self, batches: List[List[Any]]
    ) -> List[str]:
        """Process one batch per registered stream, return results."""
        results: List[str] = []
        for stream, batch in zip(self.streams, batches):
            try:
                results.append(stream.process_batch(batch))
            except StreamError as exc:
                results.append(
                    f"Stream error [{exc.stream_id}]: {exc}"
                )
        return results

    def filter_all(
        self,
        batches: List[List[Any]],
        criteria: Optional[str] = None,
    ) -> List[List[Any]]:
        """Apply each stream's filter_data() polymorphically."""
        return [
            stream.filter_data(batch, criteria)
            for stream, batch in zip(self.streams, batches)
        ]

    def collect_stats(self) -> List[Dict[str, Union[str, int, float]]]:
        """Gather get_stats() from every registered stream."""
        return [stream.get_stats() for stream in self.streams]


# ---------------------------------------------------------------------------
# Entry Point
# ---------------------------------------------------------------------------

def main() -> None:
    """Drive all demonstrations."""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()

    # ------------------------------------------------------------------ #
    # Individual stream initialisation                                    #
    # ------------------------------------------------------------------ #
    sensor: SensorStream = SensorStream("SENSOR_001")
    print("Initializing Sensor Stream...")
    print(
        f"Stream ID: {sensor.stream_id}, "
        f"Type: {sensor.stream_type}"
    )
    sensor_batch_1: List[Any] = [
        "temp:22.5", "humidity:65", "pressure:1013"
    ]
    print(f"Processing sensor batch: {sensor_batch_1}")
    try:
        print(sensor.process_batch(sensor_batch_1))
    except StreamError as exc:
        print(f"Error: {exc}")
    print()

    transaction: TransactionStream = TransactionStream("TRANS_001")
    print("Initializing Transaction Stream...")
    print(
        f"Stream ID: {transaction.stream_id}, "
        f"Type: {transaction.stream_type}"
    )
    trans_batch_1: List[Any] = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {trans_batch_1}")
    try:
        print(transaction.process_batch(trans_batch_1))
    except StreamError as exc:
        print(f"Error: {exc}")
    print()

    event: EventStream = EventStream("EVENT_001")
    print("Initializing Event Stream...")
    print(
        f"Stream ID: {event.stream_id}, "
        f"Type: {event.stream_type}"
    )
    event_batch_1: List[Any] = ["login", "error", "logout"]
    print(f"Processing event batch: {event_batch_1}")
    try:
        print(event.process_batch(event_batch_1))
    except StreamError as exc:
        print(f"Error: {exc}")
    print()

    # ------------------------------------------------------------------ #
    # Polymorphic StreamProcessor demo                                    #
    # ------------------------------------------------------------------ #
    print("=== Polymorphic Stream Processing ===")
    print(
        "Processing mixed stream types through unified interface..."
    )

    processor: StreamProcessor = StreamProcessor()
    processor.register(SensorStream("SENSOR_002"))
    processor.register(TransactionStream("TRANS_002"))
    processor.register(EventStream("EVENT_002"))

    poly_batches: List[List[Any]] = [
        ["temp:28.0", "humidity:70"],
        ["buy:200", "sell:50", "buy:300", "sell:80"],
        ["login", "error", "warning"],
    ]

    poly_results: List[str] = processor.process_all(poly_batches)
    labels: List[str] = ["Sensor", "Transaction", "Event"]
    suffixes: List[str] = [
        "readings processed",
        "operations processed",
        "events processed",
    ]

    print("Batch 1 Results:")
    for label, result, suffix in zip(labels, poly_results, suffixes):
        # Extract the numeric count from the result string
        count_str: str = result.split(":")[1].strip().split()[0]
        print(f"  - {label} data: {count_str} {suffix}")
    print()

    # ------------------------------------------------------------------ #
    # Filtering demo                                                      #
    # ------------------------------------------------------------------ #
    print("Stream filtering active: High-priority data only")

    filter_batches: List[List[Any]] = [
        ["temp:35.2", "humidity:40", "temp:38.1", "pressure:1010"],
        ["buy:50", "sell:500", "buy:20"],
        ["login", "logout"],
    ]

    sensor_filtered: List[Any] = processor.streams[0].filter_data(
        filter_batches[0], "critical"
    )
    trans_filtered: List[Any] = processor.streams[1].filter_data(
        filter_batches[1], "large"
    )

    print(
        f"Filtered results: "
        f"{len(sensor_filtered)} critical sensor alerts, "
        f"{len(trans_filtered)} large transaction"
    )
    print()

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()