from stats import get_num_words
from stats import get_char_count
from stats import sorted_list_of_dict
import sys

def get_book_text(book):
    with open(book, "r", encoding="utf-8") as f:
        file_content = f.read()
    return file_content

#def main():
    # book = "books/frankenstein.txt"
    # text = get_book_text(book)
    # print(text)


get_num_words(text=get_book_text("books/frankenstein.txt"))

char_count = get_char_count(text=get_book_text("books/frankenstein.txt"))

sorted_list_of_dict(char_count=char_count)

#main()

#print(len(sys.argv))

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
for book in sys.argv[1:]:
    text = get_book_text(book)
    get_num_words(text=text)
    char_count = get_char_count(text=text)
    sorted_list_of_dict(char_count=char_count)