import random
word_list = ['apple', 'strawberry', 'pear', 'peach', 'raspberry']
word = random.choice(word_list)
#print(word)
guess = input("guess a letter...\n")
if len(guess) == 1 and guess.isalpha():
    print("Good Guess!")
else:
    print("Oops! That is not a valid input.")