from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import strategies

Opponent = tuple[CreatureFactory, strategies.BattleStrategy]


def battle(opponents: list[tuple[CreatureFactory, strategies.BattleStrategy]]):
    print("* Battle *")

    fighters = [opponent for opponent in opponents]
    print(fighters)


if __name__ == "__main__":
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory
    flame_factory = FlameFactory()
    water_factory = AquaFactory()
    aggressive_strat = strategies.AggressiveStrategy()
    normal_strat = strategies.NormalStrategy()
    def_strat = strategies.DefensiveStrategy()

    print("*** Tournament ***")
    print("2 opponents involved")
    battle([(FlameFactory, strategies.NormalStrategy),
            (HealingCreatureFactory, strategies.DefensiveStrategy)])
