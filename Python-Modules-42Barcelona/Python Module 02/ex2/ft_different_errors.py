def garden_operations(operation_number):
    """
    Contains faulty code that raises different exception types.

    Args:
        operation_number: int from 0-3 triggers specific errors.

    Raises:
        ValueError: when operation_number is 0 (bad data conversion)
        ZeroDivisionError: when operation_number is 1 (division by zero)
        FileNotFoundError: when operation_number is 2 (non-existent file)
        TypeError: when operation_number is 3 (incompatible type mixing)
    """
    if operation_number == 0:
        # ValueError: bad data provided
        int("abc")
    elif operation_number == 1:
        # ZeroDivisionError: division by zero
        10 / 0
    elif operation_number == 2:
        # FileNotFoundError: file does not exist
        open("/non/existent/file", "r")
    elif operation_number == 3:
        # TypeError: mixing incompatible types
        "temperature: " + 25
    else:
        # No faulty code, simply return
        return


def test_error_types():
    """
    Demonstrates catching different error types and shows program continues.
    Also demonstrates catching multiple error types with one try block.
    """
    print("=== Garden Error Types Demo ===")

    # Individual error catching
    for op in range(5):
        print(f"Testing operation {op}...")
        try:
            garden_operations(op)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
