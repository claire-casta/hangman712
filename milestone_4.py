import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):               # Gives parameters of word_list and num_lives
        self.word_list = word_list                              # Allows a list of words to be input
        self.num_lives = num_lives                              # Remaining number of lives, starts at 5 automatically
        self.word = random.choice(word_list)                    # Selects a random word from the word_list
        self.num_letters = int(len(self.word))                  # Finds the number of letters in the word as an interger
        self.word_guessed = ['_'] * self.num_letters            # Creates a list with blank spaces in place of each letter in the word.
        self.list_of_guesses = []                               # Creates empty list to populate with previous guesses

    def check_guess(self, guess):                                             #function to check whether guess is in word
        if guess.lower() in self.word:                                       #converts guess to lowercase
            print(f"Good guess! {guess} is in the word.")                #tells user guess is in word
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")      #tells user guess is not in word
        

    def ask_for_input(self):
        
        while True:
            guess = input("guess a letter...\n")                               #prompts user to enter a letter guess
            if not(len(guess)) == 1 or not(guess.isalpha()):                   #checks guess is a single letter AND a-z character
                print("Invalid letter. Please, enter a single alphabetical character.")   
                #guess = input("guess a letter...\n")                        #asks user to attempt input again

            elif guess in self.list_of_guesses:                            # HELP
                print("You already tried that letter!")
                #guess = input("guess another letter...\n")                 #option for user to then choose another letter

            elif len(guess) == 1 and guess.isalpha():                         #checks guess is a single letter AND a-z character
                self.check_guess(guess)                                              # runs check_guess function
                self.list_of_guesses.append(guess)
                #break                                                          #breaks out of loop for correct guess
                #guess = input("guess another letter...\n")                 #option for user to then choose another letter
        
word_list = ['apple', 'strawberry', 'pear', 'peach', 'raspberry']
game = Hangman(word_list)
game.ask_for_input()


#print(game.word_list)
#print(game.word)
#print(game.word_guessed)
#print(game.num_lives)
#print(game.num_letters)
#print(game.list_of_guesses)

