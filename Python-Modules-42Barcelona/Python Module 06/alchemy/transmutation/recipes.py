from ..elements import create_air
from ..potions import strength_potion
import elements as root_elements

def lead_to_gold():
    return f"Recipe transmuting Lead to Gold: brew '{create_air()}' and '{strength_potion()}' mixed with '{root_elements.create_fire()}'"