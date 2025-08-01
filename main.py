from stats import get_word_count
from stats import get_char_count
from stats import sort_data
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents
    

def main():

    sys.argv

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num = get_word_count(text)
    count = get_char_count(text)
    sorted = sort_data(count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at", book_path)
    print("----------- Word Count ----------")
    print("Found", num , "total words")
    print("--------- Character Count -------")
    for items in sorted:
        print(f"{items['char']}: {items['num']}")

main() 