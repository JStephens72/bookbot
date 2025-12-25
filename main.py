import sys
from stats import count_words, count_characters, sort_characters
from my_io import validate_input, print_usage, get_file_path, print_report


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        file_contents = file_contents.replace('\ufeff','')  # Remove BOM if present
        #file_contents = file_contents.replace('\n', "") # Remove newlines
        return file_contents

def main():
    if not validate_input(sys.argv):
        print_usage()
        sys.exit(1)

    file_path = get_file_path()

    book_text = get_book_text(file_path)
    num_words = count_words(book_text)

    chars = count_characters(book_text)
    sorted_chars = sort_characters(chars)

    print_report(file_path, num_words, sorted_chars)


main()
