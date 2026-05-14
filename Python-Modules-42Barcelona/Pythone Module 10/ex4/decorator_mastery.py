from __future__ import annotations

import time
from collections.abc import Callable
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Casting {func.__name__}...')
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f'Spell completed in {duration:.3f} seconds')
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            if 'power' in kwargs:
                power = kwargs['power']
            elif len(args) == 0:
                return 'Insufficient power for this spell'
            elif isinstance(args[0], int):
                power = args[0]
            elif len(args) > 1 and isinstance(args[1], int):
                power = args[1]
            else:
                return 'Insufficient power for this spell'

            if power >= min_power:
                return func(*args, **kwargs)
            return 'Insufficient power for this spell'

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 1
            while attempt <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == max_attempts:
                        return f'Spell casting failed after {max_attempts} attempts'
                    print(f'Spell failed, retrying... (attempt {attempt}/{max_attempts})')
                    attempt += 1
            return f'Spell casting failed after {max_attempts} attempts'

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(char.isalpha() or char.isspace() for char in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:  # type: ignore[override]
        return f'Successfully cast {spell_name} with {power} power'


@spell_timer
def fireball() -> str:
    time.sleep(0.05)
    return 'Fireball cast!'


@retry_spell(3)
def unstable_spell() -> str:
    raise RuntimeError('Spell fizzled')


if __name__ == '__main__':
    print('Testing spell timer...')
    result = fireball()
    print('Result:', result)

    print('Testing retrying spell...')
    result = unstable_spell()
    print(result)

    print('Testing MageGuild...')
    print(MageGuild.validate_mage_name('Gandalf'))
    print(MageGuild.validate_mage_name('Al'))
    mage = MageGuild()
    print(mage.cast_spell('Lightning', 15))
    print(mage.cast_spell('Lightning', 5))
