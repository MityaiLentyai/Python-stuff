import random
import typing


def get_event() -> typing.Generator[tuple[str, str], None, None]:
    name_list = [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Emma",
        "Frank",
        "Grace",
        "Henry",
        "Ivy",
        "Jack",
        "Karl",
        "Leo",
        "Mia",
        "Noah",
        "Olivia",
        "Paul",
    ]
    actions_list = [
        "Sleep",
        "Eat",
        "Build",
        "Cry",
        "Code",
        "Play Dota",
    ]

    while True:
        name = random.choice(name_list)
        action = random.choice(actions_list)
        my_pair = (name, action)
        yield my_pair


def consume_event(
    collected_events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while collected_events:
        random_event = random.choice(collected_events)
        yield random_event


collected_events: list[tuple[str, str]] = []
event_generator = get_event()
for i in range(1000):
    my_tup = next(event_generator)
    collected_events.append(my_tup)
    print(f"Event {i}: Player {my_tup[0]} did action {my_tup[1]}")


ten_events: list[tuple[str, str]] = []
for i in range(10):
    my_tup = next(event_generator)
    ten_events.append(my_tup)
print(f"Built list of 10 events: {ten_events}")

event_consumator = consume_event(ten_events)
for _ in consume_event(ten_events):
    my_tup = next(event_consumator)
    ten_events.remove(my_tup)
    print(f"Got event from list: {my_tup}")
    print(f"Remains in list: {ten_events}")
