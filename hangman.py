""" hangman game guess the word from a list of words"""
import random

# creates a word made of dashes where the letter has yet to be guessed
def dashes(w, l):
    dash_add = w
    for letter in w:
        if letter in l:
            dash_add = dash_add.replace(letter, "-")
    return dash_add

# check guess is valid
def valid(l, c):
    a_to_z = "abcdefghijklmnopqrstuvwxyz"
    # check length of letter
    if len(l) != 1:
        print("You should input a single letter\n")
        return False
    # check letter is a - z
    if l not in a_to_z:
        print("It is not an ASCII lowercase letter\n")
        return False
    # check letter already typed
    if l in c:
        print("You already typed this letter\n")
        return False
    return True

#implements game
def hangman():
    # list of words, random one will be picked for each game
    lst = ["study", "sentence", "fall", "sail", "plot", "scream", "whimsical", "attack", "waves", "heat", "contribute", "hungry", "talk", "kindly", "dizzy"]
    word = lst[random.randint(0, len(lst)-1)]
    checked = []
    letters = set(word)
    dash = dashes(word, letters)
    lives = 8
    
    # gets input while you have lives left
    while lives > 0:
        print(dash)
        guess = input("Input a letter: ")
        if valid(guess, checked):
            checked.append(guess)
            if guess in letters:
                letters.remove(guess)
                dash = dashes(word, letters)
                
                if dash == word:
                    print(f"You guessed the word {word}!")
                    print("You survived!")
                    break
                print()
            else:
                print("No such letter in the word")
                lives -= 1
                if lives == 0:
                    print("You are hanged!")
                    break
                print()

#starts a new game
def start_hangman():
    print("H A N G M A N")
    while True:
        game = input('Type "play" to play the game, "exit" to quit: ')
        if game == "exit":
            return
        if game == "play":
            print()
            return hangman()
        else:
            continue

start_hangman()


