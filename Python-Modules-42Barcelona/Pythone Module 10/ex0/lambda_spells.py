from __future__ import annotations


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    power_values = list(map(lambda mage: mage['power'], mages))
    return {
        'max_power': max(power_values),
        'min_power': min(power_values),
        'avg_power': round(sum(power_values) / len(power_values), 2),
    }


if __name__ == '__main__':
    print('Testing artifact sorter...')
    artifacts = [
        {'name': 'Fire Staff', 'power': 92, 'type': 'staff'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power) comes before {sorted_artifacts[1]['name']} ({sorted_artifacts[1]['power']} power)")

    print('Testing spell transformer...')
    transformed = spell_transformer(['fireball', 'heal', 'shield'])
    print(' '.join(transformed))
