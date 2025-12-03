
def get_num_words(text):
    words = text.split()
    print(f"Found {len(words)} total words")

def get_char_count(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sorted_list_of_dict(char_count):    
    sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_chars:
        print(f"{char}: {count}")
  
     
    