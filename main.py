import sys
from stats import count_words
from stats import list_of_dictionaries
from stats import get_num_characters
from stats import sort_on
from stats import sort_list_of_dicts

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_location = sys.argv[1]


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    content = get_book_text(book_location)
    word_count = count_words(content)
    num_chars = get_num_characters(content)
    list_of_dicts = list_of_dictionaries(num_chars)

    list_of_dicts.sort(reverse=True, key=sort_on)

    final_list = sort_list_of_dicts(list_of_dicts)

    print("============ BOOKBOT ============ \n"
          f"Analyzing book found at {book_location}\n"
          "----------- Word Count ----------\n"
          f"{word_count}\n"
          "--------- Character Count -------\n"
          f"{final_list}\n"
          "============= END ===============")
    print(sys.argv)


main()
