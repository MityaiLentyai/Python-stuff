from ex1.advanced_factories import HealingCreatureFactory, \
    TransformCreatureFactory

if __name__ == "__main__":

    print("Testing Creature with healing capability base:")
    heal_factory = HealingCreatureFactory()
    small_healer = heal_factory.create_base()
    print(small_healer.describe())
    print(small_healer.attack())
    print(small_healer.heal())

    print(" evolved:")
    big_healer = heal_factory.create_evolved()
    print(big_healer.describe())
    print(big_healer.attack())
    print(big_healer.heal())

    print("\nTesting Creature with transform capability")
    transform_factory = TransformCreatureFactory()
    small_transformer = transform_factory.create_base()
    print(small_transformer.describe())
    print(small_transformer.attack())
    print(small_transformer.transform())
    print(small_transformer.attack())
    print(small_transformer.revert())

    print(" evolved:")
    big_transformer = transform_factory.create_evolved()
    print(big_transformer.describe())
    print(big_transformer.attack())
    print(big_transformer.transform())
    print(big_transformer.attack())
    print(big_transformer.revert())
    transformation_creature_factory = TransformCreatureFactory()
