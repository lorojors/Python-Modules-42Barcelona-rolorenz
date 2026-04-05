from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability


class StrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        raise NotImplementedError

    @abstractmethod
    def act(self, creature: Creature) -> List[str]:
        raise NotImplementedError


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> List[str]:
        if not self.is_valid(creature):
            raise StrategyError(f"Invalid Creature '{creature.name}' for this normal strategy")
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> List[str]:
        if not self.is_valid(creature):
            raise StrategyError(f"Invalid Creature '{creature.name}' for this aggressive strategy")
        return [creature.transform(), creature.attack(), creature.revert()]


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> List[str]:
        if not self.is_valid(creature):
            raise StrategyError(f"Invalid Creature '{creature.name}' for this defensive strategy")
        return [creature.attack(), creature.heal()]
