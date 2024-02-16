def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)

    sorted_list = []

    with open("books/frankenstein.txt", "r") as file:
        book_text = file.read()

    letters = characters_num(book_text)

    for i in letters:
        sorted_list.append({"name": i, "num": letters.get(i)})
    sorted_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of " + book_path + "---")
    print(str(get_num_words(text)) + " words found in the document")
    for i in sorted_list:
        print("The '" + i["name"] + "' character was found " + str(i["num"]) + " times")
    print("--- End report ---")

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
    
def sort_on(letters):
    return letters["num"]



main()