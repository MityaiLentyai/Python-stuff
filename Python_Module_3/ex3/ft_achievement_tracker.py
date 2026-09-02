import random


def gen_player_achivements() -> None:
    player_names = ["Emma", "Liam", "Sophia", "Ethan"]
    achivements = [
        "Monster Hunter",
        "Dragon Born",
        "Mythic Legend",
        "Shadow Ninja",
        "Gold Digger",
        "Lore Master",
        "Speed Demon",
        "Survival Expert",
        "Iron Wall",
        "Sharpshooter",
        "Ghost Walker",
        "Apex Predator",
        "Gladiator",
        "Hoarder",
        "Puzzle Solver",
        "First Blood",
        "Immortal",
        "Architect",
        "Rich Scholar",
        "Beast Tamer",
    ]
    players = []
    for name in player_names:
        count = random.randint(0, 20)
        random_achivements = random.sample(achivements, count)
        achivements_set = set(random_achivements)
        players.append(achivements_set)
        print(f"Player {name}: {achivements_set}")
    all_distinct = set.union(*players)  # star unpacks the list to avoid a loop
    print(f"\nAll distinct achievements: {all_distinct}\n")

    all_common = set.intersection(*players)
    print(f"Commom achivements: {all_common}\n")

    for name, current_set in zip(player_names, players):
        # It seems that I overcomplicated this shit, but alas
        other_sets = [p_set for p_set in players if p_set is not current_set]
        unique_to_player = current_set.difference(*other_sets)

        print(f"Only {name} has: {unique_to_player}")

    print()
    for name, current_set in zip(player_names, players):
        missing_achivements = all_distinct.difference(current_set)
        print(f"{name} is missing: {missing_achivements}")


gen_player_achivements()
