def get_num_words(book_text):
    words = book_text.split()
    count = len(words)
    return count

def get_letter_count(book_text):
    letters = {}
    for char in book_text:
        let = char.lower()
        if let in letters:
            letters[let] = letters[let] +1
        else:
            letters[let] = 1
    return letters

def sort_on(items):
    return items["num"]

def the_sorter(letters):
    new_letters = []
    for key, value in letters.items():
        if key.isalpha():
            new_letters.append({"char":key, "num":value})
    new_letters.sort(reverse=True, key=sort_on)
    return new_letters