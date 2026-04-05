from elements import create_water

def ft_alembic_1():
    return create_water()

if __name__ == "__main__":
    print("=== Alembic 1 ===")
    print("Using: 'from ... import ...' structure to access elements.py")
    print(f"Testing create_water: {ft_alembic_1()}")