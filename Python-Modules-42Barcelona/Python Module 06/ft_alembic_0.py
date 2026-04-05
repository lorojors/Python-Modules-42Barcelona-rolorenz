import elements

def ft_alembic_0():
    return elements.create_fire()

if __name__ == "__main__":
    print("=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")
    print(f"Testing create_fire: {ft_alembic_0()}")