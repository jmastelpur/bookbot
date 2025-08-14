from stats import word_count, number_of_characters, sorted_dictionaries

def get_book_text(file_path):

    with open(file_path) as f:
        text = f.read()

    return text

def main():
    text = get_book_text("books/frankenstein.txt")
    number = word_count(text)
    characters = number_of_characters(text)
    characters_sorted = sorted_dictionaries(characters)
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at books/frankenstein.txt\n")
    print("----------- Word Count ----------\n")
    print(f"Found {number} total words\n")
    print("----------- Character Count -----------\n")
    for char, count in characters_sorted.items():
        print(f"{char}: {count}\n")
    print("============= END ===============")
main()