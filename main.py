def get_book_text():
    with open("books/frankenstein.txt", "r", encoding="utf-8") as f:
        text = f.read()
    return text

