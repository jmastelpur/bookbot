def word_count(text):

    return len(text.split())

def number_of_characters(text):

    lowercase_text = text.lower()
    letters = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 
        'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, 'æ': 0, 'â': 0, 'ê': 0, 'ë': 0, 'ô': 0
    }

    for char in lowercase_text:
        if char in letters:
            letters[char] += 1

    return letters

def sorted_dictionaries(letters):

    return dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))
