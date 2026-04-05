from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print("base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print("evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    print("base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print("evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    test_healing(HealingCreatureFactory())
    test_transform(TransformCreatureFactory())
