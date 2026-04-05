import alchemy.elements

def ft_alembic_2():
    return alchemy.elements.create_earth()

if __name__ == "__main__":
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print(f"Testing create_earth: {ft_alembic_2()}")