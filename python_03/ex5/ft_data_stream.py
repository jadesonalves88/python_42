import random
import typing


PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = [
    "run", "eat", "sleep", "grab", "move",
    "climb", "swim", "release", "use",
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name: str = random.choice(PLAYERS)
        action: str = random.choice(ACTIONS)
        yield (name, action)


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        idx: int = random.randrange(len(events))
        yield events.pop(idx)


def main() -> None:
    print("=== Game Data Stream Processor ===")

    generator: typing.Generator[tuple[str, str], None, None] = gen_event()
    for i in range(1000):
        event: tuple[str, str] = next(generator)
        print(
            f"Event {i}: Player {event[0]} did action {event[1]}"
        )

    stored: list[tuple[str, str]] = []
    gen2: typing.Generator[tuple[str, str], None, None] = gen_event()
    for _ in range(10):
        stored.append(next(gen2))
    print(f"Built list of 10 events: {stored}")

    consumer: typing.Generator[tuple[str, str], None, None] = (
        consume_event(stored)
    )
    for evt in consumer:
        print(f"Got event from list: {evt}")
        print(f"Remains in list: {stored}")


if __name__ == "__main__":
    main()
