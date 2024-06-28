def write_to_file(file_path, lines):
    try:
        with open(file_path, 'w') as file:
            for line in lines:
                file.write(line + '\n')
        print(f"Successfully written to {file_path}.")
    except IOError:
        print(f"An error occurred while writing to the file at {file_path}.")

# Example usage
lines_to_write = ["Hello, world!", "This is a test.", "Writing to a file in Python."]
write_to_file('output.txt', lines_to_write)
