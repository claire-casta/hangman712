import random
word_list = ['apple', 'strawberry', 'pear', 'peach', 'raspberry']
word = random.choice(word_list)                                        #creates random word from list

def ask_for_input():
    guess = input("guess a letter...\n")                               #prompts user to enter a letter guess
    
    def check_guess(guess):                                             #function to check whether guess is in word
        if guess.lower() in word:                                       #converts guess to lowercase
            print(f"Good guess! {guess} is in the word.")                #tells user guess is in word
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")      #tells user guess is not in word

    while True:
        if len(guess) == 1 and guess.isalpha():                         #checks guess is a single letter AND a-z character
            #print("Good Guess!")
            #check_guess(guess)
            break                                                          #breaks out of loop for correct guess
            #guess = input("guess another letter...\n") #option for user to then choose another letter
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")   
            guess = input("guess a letter...\n")                        #asks user to attempt input again
    check_guess(guess)
ask_for_input()