import alchemy

def ft_alembic_4():
    return alchemy.create_air()

if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {ft_alembic_4()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print(f"Testing the hidden create_earth: {alchemy.create_earth()}")