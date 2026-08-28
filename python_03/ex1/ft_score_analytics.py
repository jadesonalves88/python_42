import sys


def main() -> None:
    args: list[str] = sys.argv[1:]
    print("=== Player Score Analytics ===")

    if len(args) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")
        return

    scores: list[int] = []

    for arg in args:
        try:
            score: int = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if len(scores) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")
        return

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    total: int = sum(scores)
    print(f"Total score: {total}")
    avg: float = total / len(scores)
    print(f"Average score: {avg:.1f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    score_range: int = max(scores) - min(scores)
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
