def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

from stats import count_words




def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = count_words(book)
    print(f"{num_words} words found in the document")





main()