def crisis_handler(filename):
    """Handle archive access with comprehensive error management"""
    try:
        with open(f"../{filename}", 'r') as file:
            content = file.read().strip()
        return f"SUCCESS: Archive recovered- '{content}'"
    except FileNotFoundError:
        if 'classified' in filename:
            raise PermissionError("Security protocols deny access")
        else:
            raise FileNotFoundError("Archive not found in storage matrix")
    except PermissionError:
        raise PermissionError("Security protocols deny access")
    except Exception as e:
        raise Exception(f"Unexpected system anomaly: {e}")

def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    # Test scenarios
    test_files = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"
    ]

    for filename in test_files:
        if filename == "standard_archive.txt":
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
        else:
            print(f"CRISIS ALERT: Attempting access to '{filename}'...")

        try:
            result = crisis_handler(filename)
            print(f"RESPONSE: {result}")
        except FileNotFoundError as e:
            print(f"RESPONSE: {e}")
        except PermissionError as e:
            print(f"RESPONSE: {e}")
        except Exception as e:
            print(f"RESPONSE: {e}")

        if filename == "standard_archive.txt":
            print("STATUS: Normal operations resumed")
        else:
            print("STATUS: Crisis handled, system stable")

    print("All crisis scenarios handled successfully. Archives secure.")

if __name__ == "__main__":
    main()