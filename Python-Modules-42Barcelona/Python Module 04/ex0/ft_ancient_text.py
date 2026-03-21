def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    filename = "../ancient_fragment.txt"

    try:
        file = open(filename, 'r')
        print(f"Accessing Storage Vault: ancient_fragment.txt")
        print("Connection established...")
        print("RECOVERED DATA:")

        content = file.read()
        print(content)

        file.close()
        print("Data recovery complete. Storage unit disconnected")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")

if __name__ == "__main__":
    main()