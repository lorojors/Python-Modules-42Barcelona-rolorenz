import sys

def main():
    print("=== Command Quest ===")
    
    program_name = sys.argv[0].split('\\')[-1]  # Get just the filename
    total_args = len(sys.argv)
    num_arguments = total_args - 1  # Exclude program name
    
    if num_arguments == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {num_arguments}")
        for i, arg in enumerate(sys.argv[1:], 1):
            print(f"Argument {i}: {arg}")
    
    print(f"Program name: {program_name}")
    print(f"Total arguments: {total_args}")

if __name__ == "__main__":
    main()