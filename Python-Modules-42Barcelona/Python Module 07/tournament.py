from typing import List, Tuple

from ex0.factory import AquaFactory, CreatureFactory, FlameFactory
from ex1.factory import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    NormalStrategy,
    StrategyError,
)


def describe_opponent(factory: CreatureFactory, strategy_name: str) -> str:
    creature = factory.create_base()
    return f"({creature.name}+{strategy_name})"


def run_tournament(opponents: List[Tuple[CreatureFactory, BattleStrategy]], title: str) -> None:
    print(title)
    labels = [describe_opponent(factory, strategy.__class__.__name__.replace("Strategy", "")) for factory, strategy in opponents]
    print(f"[ {', '.join(labels)} ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for index in range(len(opponents)):
        for opponent_index in range(index + 1, len(opponents)):
            print("* Battle *")
            factory_a, strategy_a = opponents[index]
            factory_b, strategy_b = opponents[opponent_index]
            creature_a = factory_a.create_base()
            creature_b = factory_b.create_base()
            print(creature_a.describe())
            print("vs.")
            print(creature_b.describe())
            print("now fight!")
            try:
                for line in strategy_a.act(creature_a):
                    print(line)
                for line in strategy_b.act(creature_b):
                    print(line)
            except StrategyError as error:
                print(f"Battle error, aborting tournament: {error}")
                return


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    run_tournament(
        [
            (flame_factory, NormalStrategy()),
            (healing_factory, DefensiveStrategy()),
        ],
        "Tournament 0 (basic)",
    )

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print("2 opponents involved")
    print("* Battle *")
    flame = flame_factory.create_base()
    sprout = healing_factory.create_base()
    print(flame.describe())
    print("vs.")
    print(sprout.describe())
    print("now fight!")
    try:
        for line in AggressiveStrategy().act(flame):
            print(line)
        for line in DefensiveStrategy().act(sprout):
            print(line)
    except StrategyError as error:
        print(f"Battle error, aborting tournament: {error}")

    run_tournament(
        [
            (aqua_factory, NormalStrategy()),
            (healing_factory, DefensiveStrategy()),
            (transform_factory, AggressiveStrategy()),
        ],
        "Tournament 2 (multiple)",
    )
