# import sys


# def script() -> None:

#     scores = []
#     print("=== Player Score Analytics ===")
#     for x in sys.argv[1:]:
#         try:
#             scores.append(int(x))
#         except Exception:
#             print(f"Invalid parameter: '{x}'")
#             continue
#     if len(scores) == 0:
#         print("No scores provided.", end="")
#         print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
#         return
#     try:
#         print(f"Scores processed {scores}")
#         print(f"Total score: {sum(scores)}")
#         print(f"Total players: {len(scores)}")
#         print(f"Total score: {sum(scores)}")
#         print(f"Average score: {(sum(scores))/(len(scores))}")
#         print(f"High score: {max(scores)}")
#         print(f"Low score: {min(scores)}")
#         print(f"Score range: {max(scores)-min(scores)}")
#     except Exception:
#         print("SOME FUCKING ERROR AGAIN")


# script()

import sys


def try_int(val: str) -> int | None:
    try:
        return int(val)
    except Exception:
        print(f"Invalid parameter: '{val}'")
        return None


def script() -> None:
    print("=== Player Score Analytics ===")
    processed = [try_int(x) for x in sys.argv[1:]]
    scores = [score for score in processed if score is not None]

    if len(scores) == 0:
        print("No scores provided. ", end="")
        print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    try:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {(sum(scores))/(len(scores))}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores)-min(scores)}")
    except Exception:
        print("SOME FUCKING ERROR AGAIN")


script()
