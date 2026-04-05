from .elements import create_earth, create_air
import elements as root_elements

def healing_potion():
    return f"Healing potion brewed with '{create_earth()}' and '{create_air()}'"

def strength_potion():
    return f"Strength potion brewed with '{root_elements.create_fire()}' and '{root_elements.create_water()}'"