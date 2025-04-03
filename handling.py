# Function to read, modify, and write to a new file
def read_and_write_file(input_filename, output_filename):
    try:
        # Attempt to open the input file for reading
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Attempt to open the output file for writing
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content has been written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: Could not read from '{input_filename}' or write to '{output_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main program
def main():
    # Ask the user for the filename to read from
    input_filename = input("Enter the name of the file to read from: ")

    # Ask the user for the name of the new file to write to
    output_filename = input("Enter the name of the file to write to: ")

    # Call the function to read and write the file
    read_and_write_file(input_filename, output_filename)

# Run the program
if __name__ == "__main__":
    main()
