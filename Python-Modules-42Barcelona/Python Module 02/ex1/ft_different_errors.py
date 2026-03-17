def garden_operations(operation_type):
    if operation_type == "value":
        int("abc")  # This will raise ValueError
    elif operation_type == "zero":
        1 / 0  # This will raise ZeroDivisionError
    elif operation_type == "file":
        open("nonexistent.txt")  # This will raise FileNotFoundError
    elif operation_type == "key":
        {}["missing"]  # This will raise KeyError

def test_error_types():
    print("Testing different error types in garden operations:")
    
    operations = [
        ("value", "ValueError: Occurs when trying to convert invalid data to a number, like 'abc' to int."),
        ("zero", "ZeroDivisionError: Occurs when attempting to divide by zero."),
        ("file", "FileNotFoundError: Occurs when trying to open a file that doesn't exist."),
        ("key", "KeyError: Occurs when accessing a dictionary key that doesn't exist.")
    ]
    
    for op, explanation in operations:
        print(f"\nTesting {op} error:")
        try:
            garden_operations(op)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
            print(explanation)
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
            print(explanation)
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
            print(explanation)
        except KeyError as e:
            print(f"Caught KeyError: {e}")
            print(explanation)
        print("Program continues after handling the error!")
    
    print("\nDemonstrating catching multiple error types with one except block:")
    try:
        garden_operations("value")  # This will raise ValueError
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError) as e:
        print(f"Caught one of the garden errors: {type(e).__name__}: {e}")
        print("This except block handles ValueError, ZeroDivisionError, FileNotFoundError, and KeyError together.")
    print("Program still running after the combined error handling!")

if __name__ == "__main__":
    test_error_types()