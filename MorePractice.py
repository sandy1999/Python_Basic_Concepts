"""
A py script for more rigrous practice and learn what you have gone with so far
"""

# functions to break words 
def break_words(stuff):
    """This function will break up the words for us """
    words = stuff.split(' ')
    return words

# function to sort the given word
def sort_words(words):
    """Sort the words"""
    return sorted(words)

# function to pop first word from the list
def print_first_word(words):
    """Pop first word from the list of words and returns it"""
    word = words.pop(0)
    print(word)

# function to pop  the last word from the list  
def print_last_word(words):
    """ Pop the last word form the list of words and return it"""
    print(words.pop(-1))

# a function to sort the words of scenteces
def sort_sentence(sentence):
    """ Sort words of the sentence"""
    words = break_words(sentence)
    return sort_words(words)

# function to print last and first words of a sentence
def print_first_and_last(sentence):
    """Takes a sentecne and return first and last word of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

# function to print last and first of the sorted sentence
def print_first_and_last_sorted(sentence):
    """ Takes a sentence and print first and last sorted words"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)