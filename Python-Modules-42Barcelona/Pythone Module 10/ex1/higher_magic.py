from __future__ import annotations

from collections.abc import Callable

Spell = Callable[[str, int], str]
SpellSequence = Callable[[str, int], list[str]]


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not callable(spell1) or not callable(spell2):
        raise TypeError('spell1 and spell2 must be callable')

    def combined(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not callable(base_spell):
        raise TypeError('base_spell must be callable')

    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not callable(condition) or not callable(spell):
        raise TypeError('condition and spell must be callable')

    def cast_if(target: str, power: int) -> str:
        return spell(target, power) if condition(target, power) else 'Spell fizzled'

    return cast_if


def spell_sequence(spells: list[Callable]) -> Callable:
    if not all(callable(spell) for spell in spells):
        raise TypeError('all items in spells must be callable')

    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return sequence


def fireball(target: str, power: int) -> str:
    return f'Fireball hits {target} for {power} damage'


def heal(target: str, power: int) -> str:
    return f'Heals {target} for {power} HP'


def shield(target: str, power: int) -> str:
    return f'Shield protects {target} with {power} defense'


def is_powerful(target: str, power: int) -> bool:
    return power >= 30


if __name__ == '__main__':
    print('Testing spell combiner...')
    combined = spell_combiner(fireball, heal)
    combined_result = combined('Dragon', 50)
    print('Combined spell result:', ', '.join(combined_result))

    print('Testing power amplifier...')
    boosted_fireball = power_amplifier(fireball, 3)
    original = fireball('Goblin', 10)
    amplified = boosted_fireball('Goblin', 10)
    print('Original:', original)
    print('Amplified:', amplified)

    print('Testing conditional caster...')
    conditional_spell = conditional_caster(is_powerful, shield)
    print(conditional_spell('Knight', 20))
    print(conditional_spell('Knight', 40))

    print('Testing spell sequence...')
    sequence = spell_sequence([fireball, heal, shield])
    print(sequence('Hero', 25))
