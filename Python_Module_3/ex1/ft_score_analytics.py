import sys

# class No_scores(Exception):
#     def print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...
# ")


def script() -> None:
    print("=== Player Score Analytics ===")
    scores = [None] * len(sys.argv)
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ", end="")
        print("ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed {sys.argv[1:]}")
        print(f"Total score: {sum(scores)}")

    # i: int = 1
    # while i < len(sys.argv):
    #     print(f"Argument {i}: {sys.argv[i]}")
    #     i += 1

    print(f"Total players: {len(sys.argv)-1}")


script()
