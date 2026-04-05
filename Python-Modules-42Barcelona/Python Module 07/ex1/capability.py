from __future__ import annotations

from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str = "itself") -> str:
        raise NotImplementedError


class TransformCapability(ABC):
    def __init__(self) -> None:
        self._transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def revert(self) -> str:
        raise NotImplementedError

    def is_transformed(self) -> bool:
        return self._transformed
