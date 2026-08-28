"""Higher Realm: higher-order functions that operate on other functions."""

from collections.abc import Callable

Spell = Callable[[str, int], str]


def spell_combiner(
    spell1: Spell, spell2: Spell
) -> Callable[[str, int], tuple[str, str]]:
    """Return a spell that casts both spells and returns both results."""
    def combined(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)

    return combined


def power_amplifier(base_spell: Spell, multiplier: int) -> Spell:
    """Return a spell whose power is multiplied before being cast."""
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(condition: Callable, spell: Spell) -> Spell:
    """Return a spell that only casts when the condition is true."""
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional


def spell_sequence(spells: list[Spell]) -> Callable[[str, int], list[str]]:
    """Return a spell that casts every spell and returns their results."""
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return sequence


def _fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def _heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def _shield(target: str, power: int) -> str:
    return f"Shield protects {target} with {power} armor"


def main() -> None:
    """Demonstrate every higher-order spell modifier."""
    print("Testing spell combiner...")
    combined = spell_combiner(_fireball, _heal)
    fire_result, heal_result = combined("Dragon", 30)
    print(f"Combined spell result: {fire_result}, {heal_result}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(_fireball, 3)
    print("Original: 10, Amplified: 30")
    print(mega_fireball("Dragon", 10))

    print("\nTesting conditional caster...")
    guarded_heal = conditional_caster(
        lambda target, power: power > 0, _heal
    )
    print(guarded_heal("Knight", 20))
    print(guarded_heal("Knight", 0))

    print("\nTesting spell sequence...")
    combo = spell_sequence([_fireball, _shield, _heal])
    for result in combo("Dragon", 15):
        print(result)


if __name__ == "__main__":
    main()
