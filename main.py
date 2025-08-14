def get_book_text(file_path):

    with open(file_path) as f:
        text = f.read()

    return text


def main():
    book_text = get_book_text("/home/jmast/workspace/github.com/Jmastelpur/bookbot/frankenstein.txt")
    print(book_text)