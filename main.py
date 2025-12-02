def get_book_text(book):
    with open(book, "r", encoding="utf-8") as f:
        file_content = f.read()
    return file_content

def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    print(text)
    
    
main()