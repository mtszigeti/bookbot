def main():
    book_path = "books/frankenstein.rtf"
    text = get_book_text(book_path)
    print(text)

def get_num_words(text):
    words = text.split()
    return len(words)

def characters_num(text):
    lower_case_text = text.lower()
    letters = {}
    for char in lower_case_text:
        if char.isalpha():
            letters[char] = letters.get(char, 0) + 1
    return letters

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()