from stats import wordCount, characterCount, sort_num
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    BookCode = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def print_num_words():
    num_words = wordCount(get_book_text(BookCode))
    return print(f"Found {num_words} total words")

def plain_print_char():
    num_characters = characterCount(get_book_text(BookCode))
    return print(sort_num(num_characters))

def main():
    num_characters = characterCount(get_book_text(BookCode))
    sort_num(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {BookCode}...")
    print("----------- Word Count ----------")
    print_num_words()
    print("--------- Character Count -------")
    for d in sort_num(num_characters):
        letter = d["char"]
        count = d["num"]
        print(f"{letter}: {count}")
    print("============= END ===============")
    return
   
main()
