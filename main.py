def get_book_text(book):
    with open(book, "r", encoding="utf-8") as f:
        file_content = f.read()
    return file_content

def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    print(text)

def num_words(text):
    words = text.split()
    print(f"Found {len(words)} total words")

num_words(text=get_book_text("books/frankenstein.txt"))
    
    
main()