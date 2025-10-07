from stats import count_book_words
from stats import character_count
from stats import sort_character_count

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def print_report(book_file):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}")
    book_text = get_book_text('books/frankenstein.txt')
    num_words = count_book_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_char_count = sort_character_count(character_count(book_text))
    for entry in sorted_char_count:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

def main():
    print_report('books/frankenstein.txt')

main()