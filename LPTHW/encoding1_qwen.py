import sys

# Unpack command-line arguments
script, input_encoding, error = sys.argv


def print_line(line, encoding, errors):
    """Encode a string to bytes and decode back; print both forms."""
    stripped_line = line.strip()
    raw_bytes = stripped_line.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<==>", cooked_string)


def main(language_file, encoding, errors):
    """Process each line in the file using a loop instead of recursion."""
    for line in language_file:
        print_line(line, encoding, errors)


# Open the file safely using 'with'
try:
    with open("languages.txt", encoding="utf-8") as languages:
        main(languages, input_encoding, error)
except FileNotFoundError:
    print("Error: languages.txt not found.")
    sys.exit(1)
except UnicodeError as e:
    print(f"Encoding error: {e}")
    sys.exit(1)
