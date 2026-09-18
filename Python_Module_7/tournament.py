from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import strategies
from ex2.strategies import BattleError
import itertools

Opponent = tuple[type[CreatureFactory], type[strategies.BattleStrategy]]


def battle(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    if len(opponents) < 2:
        print("Not enough opponents to run a tournament!")
        return

    for opponent_a, opponent_b in itertools.combinations(opponents, 2):
        factory_class_a, strategy_class_a = opponent_a
        factory_instance_a = factory_class_a()
        strategy_a = strategy_class_a()
        fighter_a = factory_instance_a.create_base()

        factory_class_b, strategy_class_b = opponent_b
        factory_instance_b = factory_class_b()
        strategy_b = strategy_class_b()
        fighter_b = factory_instance_b.create_base()
        print("\n* Battle *")
        print(
            f"{fighter_a.name} is a {fighter_a.type} type Creature\n"
            f"vs\n"
            f"{fighter_b.name} is a {fighter_b.type} type Creature")
        print(" now fight!")
        try:
            strategy_a.act(fighter_a)
            strategy_b.act(fighter_b)
        except BattleError as e:
            print(f"{e}")


if __name__ == "__main__":
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory
    flame_factory = FlameFactory()
    water_factory = AquaFactory()
    aggressive_strat = strategies.AggressiveStrategy()
    normal_strat = strategies.NormalStrategy()
    def_strat = strategies.DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(FlameFactory, strategies.NormalStrategy),
            (HealingCreatureFactory, strategies.DefensiveStrategy)])

    print("\nTournament 1(error)")
    print("[(Flameling + Aggressive), (Healing + Defensive)]")
    battle([(FlameFactory, strategies.AggressiveStrategy),
            (HealingCreatureFactory, strategies.DefensiveStrategy)])

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([(AquaFactory, strategies.NormalStrategy),
            (HealingCreatureFactory, strategies.DefensiveStrategy),
            (TransformCreatureFactory,
             strategies.AggressiveStrategy)])
