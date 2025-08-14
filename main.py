from stats import word_count, number_of_characters, sorted_dictionaries
import sys

def get_book_text(file_path):

    with open(file_path) as f:
        text = f.read()

    return text

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    number = word_count(text)
    characters = number_of_characters(text)
    characters_sorted = sorted_dictionaries(characters)
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {book_path}\n")
    print("----------- Word Count ----------\n")
    print(f"Found {number} total words\n")
    print("----------- Character Count -----------\n")
    for char, count in characters_sorted.items():
        print(f"{char}: {count}\n")
    print("============= END ===============")
main()