from ex0 import AquaFactory, CreatureFactory, FlameFactory


def check_factory(factory: CreatureFactory) -> None:
    print(f"Testing {factory.__class__.__name__}")
    for creature in (factory.create_base(), factory.create_evolved()):
        print(creature.describe())
        print(creature.attack())
    print()


def fight(factory_one: CreatureFactory, factory_two: CreatureFactory) -> None:
    first = factory_one.create_base()
    second = factory_two.create_base()

    print("Testing battle")
    print(f"{first.describe()}\n vs \n{second.describe()}")
    print(" fight!")
    print(first.attack())
    print(second.attack())


if __name__ == "__main__":
    fire_factory = FlameFactory()
    water_factory = AquaFactory()

    check_factory(fire_factory)
    check_factory(water_factory)
    fight(fire_factory, water_factory)
