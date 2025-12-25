import sys

def get_file_path():
    return sys.argv[1]

def print_report(file_path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("------------ Word Count ------------")
    print(f"Found {num_words} total words")
    print("------------ Character Count ------------")
    
    for item in sorted_chars:
        if item["char"] != "\n" and item["char"] != " ":
            print(f"{item['char']}: {item['num']}")

    return None

def validate_input(args):
    if len(args) != 2:
        return False
    return True

def print_usage():
    print("Usage: python3 main.py <path_to_book>")
    return None

