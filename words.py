def print_upper_words(words):
    """With the given array this function turns each word to uppercase and print each of them on sep line """
    
    for word in words:
        print(word.upper())


 print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])

def print_upper_words3(words):
    """With the given array this function turns each word to uppercase and print the words only which start with "E"  on each line """
    
    for word in words:
        word = word.upper()
        if word.startswith("E"):
            print(word)


 print_upper_words3(["eagle", "Edward", "Alfred"])

def print_upper_words4(words, must_start_with):
    """With the given array this function turns each word to uppercase and print the words only which start with given letter in the must_start_with dictionary  on each line """
    
    for word in words:
        word = word.upper()
        for letter in must_start_with:
            letter = letter.upper()
            if word.startswith(letter):
                print(word)

print_upper_words4(["hello", "hey", "goodbye", "yo", "yes","yolo", "heyo"],
                   must_start_with=["h", "y"])