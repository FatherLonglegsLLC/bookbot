from stats import get_num_words
from stats import get_letter_count
from stats import the_sorter
import sys

def get_book_text(filename):
  with open(filename) as f:
    contents = f.read()
    return contents

def main():
  check = len(sys.argv)
  if check != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    filename = sys.argv[1]
    book_text = get_book_text(filename)
    num_words = get_num_words(book_text)
    message = f"Found {num_words} total words found in the document"
    character_counts = get_letter_count(book_text)
    ordered = the_sorter(character_counts)
    print (message)
    #print (character_counts)
    for value in ordered:
      digit = value["char"]
      numb = value["num"]
      output = f"{digit}: {numb}"
      print (output)

main()