
def get_num_words(text):
    words = text.split()
    print(f"Found {len(words)} total words")

def get_char_count(text):
    text = text.lower()
    char_count = {}
    for char in text:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    print(char_count)

def sorted_dict():
    pass    