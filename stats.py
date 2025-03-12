def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def split_book_text(book):
    # Takes a percieved book and splits the text
    book_text = book
    split_text = book_text.split()
    
    # Loops through each word and counts the total amount of words
    num_words = 0
    for words in split_text:
        num_words += 1

    return split_text

def count_characters():
    # Lower text and use helper functions to lowercase and split text
    text = get_book_text('books/frankenstein.txt')
    lowercase_book = text.lower()
    lowercase_split_text = split_book_text(lowercase_book)

    # Initialize the dictionary
    # o: 2390
    letters = {}

    for words in lowercase_split_text:
        characters = list(words)
        
        for symbol in characters:
            
            if symbol in letters:
                letters[symbol] += 1
            else:
                letters[symbol] = 1       

    print(letters)


    


    

