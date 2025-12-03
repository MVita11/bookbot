#from stats import get_num_words
from stats import get_char_count

def get_book_text(book):
    with open(book, "r", encoding="utf-8") as f:
        file_content = f.read()
    return file_content

#def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    print(text)


#get_num_words(text=get_book_text("books/frankenstein.txt"))
get_char_count(text=get_book_text("books/frankenstein.txt"))
    
#main()