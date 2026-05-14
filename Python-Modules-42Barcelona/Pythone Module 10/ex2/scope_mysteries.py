from __future__ import annotations

from collections.abc import Callable


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total_power = initial_power

    def accumulator(additional_power: int) -> int:
        nonlocal total_power
        total_power += additional_power
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchant(item_name: str) -> str:
        return f'{enchantment_type} {item_name}'

    return enchant


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, object] = {}

    def store(key: str, value: object) -> None:
        memory[key] = value

    def recall(key: str) -> object:
        return memory.get(key, 'Memory not found')

    return {'store': store, 'recall': recall}


if __name__ == '__main__':
    print('Testing mage counter...')
    counter_a = mage_counter()
    print('counter_a call 1:', counter_a())
    print('counter_a call 2:', counter_a())
    counter_b = mage_counter()
    print('counter_b call 1:', counter_b())

    print('Testing spell accumulator...')
    accumulator = spell_accumulator(100)
    print('Base 100, add 20:', accumulator(20))
    print('Base 100, add 30:', accumulator(30))

    print('Testing enchantment factory...')
    flaming = enchantment_factory('Flaming')
    frozen = enchantment_factory('Frozen')
    print(flaming('Sword'))
    print(frozen('Shield'))

    print('Testing memory vault...')
    vault = memory_vault()
    vault['store']('secret', 42)
    print("Store 'secret' = 42")
    print("Recall 'secret':", vault['recall']('secret'))
    print("Recall 'unknown':", vault['recall']('unknown'))
