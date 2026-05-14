from __future__ import annotations

from functools import lru_cache, partial, reduce, singledispatch
from operator import add, mul, itemgetter
from typing import Any, Callable, Dict, List


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations = {
        'add': add,
        'multiply': mul,
        'max': max,
        'min': min,
    }

    if operation not in operations:
        raise ValueError(f'Unknown operation: {operation}')

    op_func = operations[operation]
    if operation in {'max', 'min'}:
        return reduce(op_func, spells)

    return reduce(op_func, spells)


def partial_enchanter(base_enchantment: Callable[[int, str, str], str]) -> Dict[str, Callable[[str], str]]:
    return {
        'fire': partial(base_enchantment, 50, 'fire'),
        'ice': partial(base_enchantment, 50, 'ice'),
        'wind': partial(base_enchantment, 50, 'wind'),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError('n must be non-negative')
    if n in {0, 1}:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatcher(spell: Any) -> str:
        return 'Unknown spell type'

    @dispatcher.register
    def _(spell: int) -> str:  # damage spell
        return f'Damage spell: {spell} damage'

    @dispatcher.register
    def _(spell: str) -> str:  # enchantment
        return f'Enchantment: {spell}'

    @dispatcher.register
    def _(spell: list) -> str:  # multi-cast
        return f'Multi-cast: {len(spell)} spells'

    return dispatcher


def base_enchantment(power: int, element: str, target: str) -> str:
    return f'{element.capitalize()} blast hits {target} with {power} power'


if __name__ == '__main__':
    print('Testing spell reducer...')
    spells = [10, 20, 30, 40]
    print('Sum:', spell_reducer(spells, 'add'))
    print('Product:', spell_reducer(spells, 'multiply'))
    print('Max:', spell_reducer(spells, 'max'))
    print('Min:', spell_reducer(spells, 'min'))

    print('Testing memoized fibonacci...')
    print('Fib(0):', memoized_fibonacci(0))
    print('Fib(1):', memoized_fibonacci(1))
    print('Fib(10):', memoized_fibonacci(10))
    print('Fib(15):', memoized_fibonacci(15))

    print('Testing spell dispatcher...')
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher('fireball'))
    print(dispatcher(['spark', 'flare', 'pulse']))
    print(dispatcher({}))
