"""Ancient Library: treasures of the functools and operator modules."""

import operator
from collections.abc import Callable
from functools import lru_cache, partial, reduce, singledispatch
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce a list of spell powers using the given operation."""
    if not spells:
        return 0
    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }
    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """Return element enchantments with power pre-filled to 50."""
    elements = ("fire", "ice", "lightning")
    return {
        element: partial(base_enchantment, 50, element)
        for element in elements
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using memoization."""
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@singledispatch
def _cast_spell(spell: object) -> str:
    return "Unknown spell type"


@_cast_spell.register
def _cast_damage(spell: int) -> str:
    return f"Damage spell: {spell} damage"


@_cast_spell.register
def _cast_enchantment(spell: str) -> str:
    return f"Enchantment: {spell}"


@_cast_spell.register
def _cast_multicast(spell: list) -> str:
    return f"Multi-cast: {len(spell)} spells"


def spell_dispatcher() -> Callable[[Any], str]:
    """Return the singledispatch spell caster."""
    return _cast_spell


def main() -> None:
    """Demonstrate the functools artifacts."""
    print("Testing spell reducer...")
    powers = [10, 20, 40]
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")
    print(f"Min: {spell_reducer(powers, 'min')}")

    print("\nTesting partial enchanter...")

    def enchant(power: int, element: str, target: str) -> str:
        return f"{element.capitalize()} {target} (+{power} power)"

    enchanters = partial_enchanter(enchant)
    print(enchanters["fire"]("Dragon"))
    print(enchanters["ice"]("Golem"))
    print(enchanters["lightning"]("Golem"))

    print("\nTesting memoized fibonacci...")
    for value in (0, 1, 10, 15):
        print(f"Fib({value}): {memoized_fibonacci(value)}")
    print(memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")
    cast = spell_dispatcher()
    print(cast(42))
    print(cast("fireball"))
    print(cast(["fireball", "heal", "shield"]))
    print(cast(3.14))


if __name__ == "__main__":
    main()
