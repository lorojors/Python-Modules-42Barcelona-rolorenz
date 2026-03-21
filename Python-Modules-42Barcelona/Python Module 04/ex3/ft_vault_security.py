def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    # Secure extraction using context manager
    print("SECURE EXTRACTION:")
    with open("../classified_data.txt", 'r') as file:
        content = file.read()
        print(content)

    # Secure preservation using context manager
    print("SECURE PRESERVATION:")
    with open("../security_protocols.txt", 'w') as file:
        file.write("[CLASSIFIED] New security protocols archived\n")
        print("[CLASSIFIED] New security protocols archived")

    print("Vault automatically sealed upon completion")
    print("All vault operations completed with maximum security")

if __name__ == "__main__":
    main()