import sys

def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    # Collect input
    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")

    # Output to standard stream
    sys.stdout.write(f"[STANDARD] Archive status from {archivist_id}: {status_report}\n")

    # Output alert to error stream
    sys.stderr.write("[ALERT] System diagnostic: Communication channels verified\n")

    # Final standard message
    sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("Three-channel communication test successful")

if __name__ == "__main__":
    main()