import random

player_list = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam",
]

print(f"Initial list of players: {player_list}")

new_list = [cap.capitalize() for cap in player_list]
print(f"New list with all names capitalized: {new_list}")

newest_list = [cap for cap in player_list if cap == cap.capitalize()]
print(f"New list of capitalized names only: {newest_list}")

score_dict = {name: random.randint(1, 1000) for name in player_list}
print(f"Score dict: {score_dict}")

score_average = round(sum(score_dict.values()) / len(score_dict), 2)
print(f"Score average is " f"{score_average}")
high_scores = {key: value for key, value
               in score_dict.items() if value > score_average}
print(f"High scores: {high_scores}")
