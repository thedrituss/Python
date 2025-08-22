from sys import argv

# Unpack command-line arguments
script, input_file = argv


def print_all(f):
    """Print the entire contents of the file."""
    print(f.read())


def rewind(f):
    """Reset file pointer to the beginning."""
    f.seek(0)


def print_a_line(line_count, f):
    """Print a single line with line number."""
    print(line_count, f.readline(), end="")  # Avoid double newlines


# Open and use the file
with open(input_file) as current_file:
    print("First let's print the whole file:\n")
    print_all(current_file)

    print("\nNow let's rewind, kind of like a tape.")
    rewind(current_file)

    print("\nLet's print three lines:")
    for current_line in range(1, 4):
        print_a_line(current_line, current_file)

