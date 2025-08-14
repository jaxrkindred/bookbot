import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

from stats import count_words
from stats import character_count
from stats import sorted_list



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = get_book_text(sys.argv[1])
        num_words = count_words(book)
        characters = character_count(book)
        for_report = sorted_list(characters)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for dict in for_report:
            char = dict["char"]
            count = dict["num"]
            print(f"{char}: {count}")


        print("============= END ===============")






main()