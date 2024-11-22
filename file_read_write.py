def main():
    import os

    print("Welcome to the File Read & Write Challenge 🖋️!")

    # Ask the user for the input filename
    input_file = input("Enter the name of the file to read: ")

    try:
        # Check if the file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"The file '{input_file}' does not exist.")

        # Read the file
        with open(input_file, 'r') as file:
            content = file.readlines()

        # Modify the content (e.g., prepend line numbers)
        modified_content = [f"{i+1}: {line}" for i, line in enumerate(content)]

        # Ask the user for the output filename
        output_file = input("Enter the name of the file to write the modified content to: ")

        # Write the modified content to the new file
        with open(output_file, 'w') as file:
            file.writelines(modified_content)

        print(f"The modified content has been written to '{output_file}'.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError:
        print("Error: You don't have permission to access this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
