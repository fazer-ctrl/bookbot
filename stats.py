def get_book_text(filepath):
    with open(filepath) as f:
        return f.read(), filepath

def split_book_text(book):
    split_text = book.split()
    num_words = len(split_text)
    return split_text, num_words

def count_characters(filepath):
    text, path = get_book_text(filepath)
    lowercase_book = text.lower()
    lowercase_split_text, num_words = split_book_text(lowercase_book)

    letters = {}
    for word in lowercase_split_text:
        for symbol in word:
            letters[symbol] = letters.get(symbol, 0) + 1

    return letters, num_words, text, path

def word_report(filepath):
    characters, num_words, text, path = count_characters(filepath)

    print("============ BOOKBOT ============\n"
          f"Analyzing book found at {path}\n"
          "----------- Word Count -----------\n"
          f"Found {num_words} total words\n"
          "--------- Character Count ---------")

    sorted_items = sorted(characters.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_items:
        print(f"{char}: {count}")

    print("============= END ===============")




    


    

