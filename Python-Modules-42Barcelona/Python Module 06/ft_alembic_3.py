from alchemy.elements import create_air

def ft_alembic_3():
    return create_air()

if __name__ == "__main__":
    print("=== Alembic 3 ===")
    print("Accessing alchemy/elements.py using 'from ... import ...' structure")
    print(f"Testing create_air: {ft_alembic_3()}")