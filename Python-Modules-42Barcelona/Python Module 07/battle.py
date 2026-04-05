from ex0 import AquaFactory, CreatureFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()
    print(base_creature.describe())
    print(base_creature.attack())
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def test_battle(flame_factory: CreatureFactory, aqua_factory: CreatureFactory) -> None:
    print("Testing battle")
    flame = flame_factory.create_base()
    aqua = aqua_factory.create_base()
    print(flame.describe())
    print("vs.")
    print(aqua.describe())
    print("fight!")
    print(flame.attack())
    print(aqua.attack())


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    test_factory(flame_factory)
    test_factory(aqua_factory)
    test_battle(flame_factory, aqua_factory)
