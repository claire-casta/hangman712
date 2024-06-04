import random

class Hangman:
    """This class is used to create a hangman game, with the computer randomly selecting a word from the word_list and the user tries to guess that 
        word within a certain amount of attempts. 
        
        - If the user guesses correctly, the game will tell them how many unique letters are left to guess and prompt them to guess again. 
        - If the user guesses incorrectly, the game will tell them this, show how many lives they have remaining and then prompt them to guess again.
        - If an invalid guess is entered the game will tell the user and prompt them to guess again.
        - If a previous guess is repeated, the game will tell the user, list their previous guesses and prompt them to guess again.
        - The user must guess the word before they run out of lives to win the game.
        - If the user runs out of lives they lose the game.

        Attributes
        ----------
       word_list : list
            a list of words for the computer to randomly choose from
        num_lives : int
            the number of lives remaining, defaults automatically to 5.
        word : any
            the randomly selected word from 'word_list'
        num_letters : int
            the number of unique letters left to guess in 'word'
        word_guessed : list[str]
            a list showing a blank space for each letter in 'word'. Replaced by letter once correctly guessed.
        list_of_guesses : list
            an empty list to be populated with previous guesses

        Methods
        -------
        __check_guess__(guess)
            Checks whether the letter guessed is in the word, and prints a response.
        __ask_for_input__()
            Asks the user to guess a letter in the word, and then checks whether the letter guessed is a valid input.
        """
        
    def __init__(self, word_list, num_lives = 5):                               # Gives parameters of word_list and num_lives
        """
        Parameters
        ----------
        word_list : list
            A list of words for the computer to randomly choose from (a short example list is provided which can be replaced by the user)
        num_lives : int, optional
            Number of lives remaining (defaults is 5)
        """

        self.word_list = word_list                                              # Allows a list of words to be input
        self.num_lives = num_lives                                              # Remaining number of lives, starts at 5 automatically
        self.word = random.choice(word_list)                                    # Selects a random word from the word_list
        self.num_letters = int(len(set(self.word)))                             # Finds the number of unique letters in the word as an interger
        self.word_guessed = ['_'] * (len(self.word))                            # Creates a list with blank spaces in place of each letter in the word.
        self.list_of_guesses = []                                               # Creates empty list to populate with previous guesses

    def __check_guess__(self, guess):                                           #function to check whether guess is in word
        """
        Checks whether the letter guessed is in the word, and prints a response.
        - If the user guesses correctly the game will confirm this, print the word with guessed letters and blank spaces as well as how many unique letters are left to guess.
        - If the user guesses incorrectly the game will say so, prompt to guess again, reduce the number of remaining lives by one and print how many lives are left. 
        
        Parameters
        ----------
        guess : any
            user guess, must be a single a-z letter
        """
        
        if guess.lower() in self.word:                                          #converts guess to lowercase
            print(f"Good guess! {guess} is in the word.")                       #tells user guess is in word
            while True:
                for i in range(len(self.word)):                                 # Ensures all letters within selected word are checked, using the length of the word
                    if self.word[i] == guess:                                   # If letter guessed IS found within the randomly selected word
                        self.word_guessed[i] = guess                            # Replaces blank letter in word with the correctly guesed letter at the correct index/indeces
                break
            self.num_letters -= 1                                               # Reduces the number of letters left to guess
            print(self.word_guessed)                                            # prints word with guessed letters and blank spaces
            print(f"You have {self.num_letters} unique letters left to guess")  # prints number of unique letters left to guess
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")             # Tells user guess is not in word
            self.num_lives -= 1                                                 # Reduces the number of lives left
            print(f"You have {self.num_lives} lives left")                      # Tells user how many lives left

    def __ask_for_input__(self):
        """
        Asks the user to guess a letter in the word, and then checks whether the letter guessed is a valid input. 
        A valid input is a single alphbetical letter.
        - If the user guess is NOT a single letter or NOT a-z, the game will say the guess is invalid and prompt to guess again.
        - If the user repeats a previous guess, the game will say this, print a list of previous guesses as a reminder and prompt to guess again.
        - If the guess is valid, it will check whether it is correct using the __check_guess__ function, then append the guess to the list of previous guesses.
        
        Parameters
        ----------
        guess : any
            user guess, must be a single a-z letter
        """
        while True:
            guess = input("guess a letter...\n")                                # Prompts user to enter a letter guess
            if not(len(guess)) == 1 or not(guess.isalpha()):                    # If guess is NOT a single letter AND a-z character
                print("Invalid letter. Please, enter a single alphabetical character.")   
                break                                                           # Prompts user to enter a single alphabetical character
            elif guess in self.list_of_guesses:                                 # If guess IS in list of previous guesses
                print("You already tried that letter!")                         # Prompts user to try another letter
                print(f"Previous guesses: {self.list_of_guesses}")              # Prints list of previous guesses to remind user
                break
            elif len(guess) == 1 and guess.isalpha():                           # Checks guess is a single letter AND a-z character
                self.__check_guess__(guess)                                     # Runs check_guess function
                self.list_of_guesses.append(guess)                              # Adds guess to list of previous guesses
                break


def play_game(word_list):
    """
    Sets the number of lives.
    Calls the Hangman Class using the variable 'game'.
    Defines the win or lose criteria:
    - If the number of lives drops to zero, the game will tell the user "You lost!"
    - If the number of lives is greater than zero AND there are no more unique letters left to guess, the game will tell the user "Congratulations! You won the game!"
    - If the number of lives is greater than zero AND there are still unique letters left to guess, the game will ask call the __ask_for_input__ function, starting the guessing process again.
    
    Parameters
    ----------
    word_list : list[str]
    """

    num_lives = 5
    game = Hangman(word_list, num_lives)
    print(game.word_guessed)
    while True:
        if game.num_lives <= 0:
            print("You lost!")
            break
        elif game.num_lives >= 0 and game.num_letters <= 0:
            print("Congratulations! You won the game!")
            break
        elif game.num_letters > 0:
            game.__ask_for_input__()

#help(Hangman)                                                                  # Optional call for help via docstrings

word_list = ['pineapple', 'strawberry', 'blackberry', 'blueberry', 'raspberry'] # Editable list of words for computer to choose from
play_game(word_list)                                                            # Starts the game
