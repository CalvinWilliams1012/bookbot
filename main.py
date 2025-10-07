from stats import count_book_words
from stats import character_count

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    book_text = get_book_text('books/frankenstein.txt')
    num_words = count_book_words(book_text)
    print(f"Found {num_words} total words")
    print(character_count(book_text))

main()