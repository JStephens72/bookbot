def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    chars = {}
    for char in text:
        char = char.lower()
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars

def sort_on(items):
    return items["num"]

def sort_characters(chars):
    char_list = []

    for char, count in chars.items():
        char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)

    return char_list