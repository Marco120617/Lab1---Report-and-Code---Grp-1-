def navigate_file():
    try:
        # Prompt the user for a filename
        filename = input("Enter the filename: ").strip()
        
        # Open the file and read the lines into a list
        with open(filename, 'r') as file:
            lines = file.readlines()

        print(f"The file has {len(lines)} lines.")
        
        # Loop to prompt for line numbers
        while True:
            line_number = int(input("Enter a line number (0 to quit): "))
            
            if line_number == 0:
                print("Program exiting.")
                break
            elif 1 <= line_number <= len(lines):
                print(f"Line {line_number}: {lines[line_number - 1].strip()}")
            else:
                print(f"Invalid input. Please enter a number between 1 and {len(lines)}.")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    navigate_file()
