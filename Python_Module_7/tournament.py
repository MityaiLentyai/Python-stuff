from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import strategies
from ex2.strategies import BattleError

Opponent = tuple[CreatureFactory, strategies.BattleStrategy]


def battle(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    if len(opponents) < 2:
        print("Not enough opponents to run a tournament!")
        return

    for index, opponent_a in enumerate(opponents):
        for opponent_b in opponents[index + 1:]:
            factory_a, strategy_a = opponent_a
            fighter_a = factory_a.create_base()

            factory_b, strategy_b = opponent_b
            fighter_b = factory_b.create_base()
            print("\n* Battle *")
            print(
                f"{fighter_a.name} is a {fighter_a.type} type Creature\n"
                f" vs\n"
                f"{fighter_b.name} is a {fighter_b.type} type Creature")
            print(" now fight!")
            try:
                strategy_a.act(fighter_a)
                strategy_b.act(fighter_b)
            except BattleError as e:
                print(f"{e}")


if __name__ == "__main__":

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(FlameFactory(), strategies.NormalStrategy()),
            (HealingCreatureFactory(), strategies.DefensiveStrategy())])

    print("\nTournament 1(error)")
    print("[(Flameling + Aggressive), (Healing + Defensive)]")
    battle([(FlameFactory(), strategies.AggressiveStrategy()),
            (HealingCreatureFactory(), strategies.DefensiveStrategy())])

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([(AquaFactory(), strategies.NormalStrategy()),
            (HealingCreatureFactory(), strategies.DefensiveStrategy()),
            (TransformCreatureFactory(), strategies.AggressiveStrategy())])
