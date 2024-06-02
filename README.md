# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Installation instructions
This game is implemented using Python.
Run the game using a terminal compatible with Python (eg, bash) and run the command 'Hangman_Game.py' (if using Windows).

## Usage instructions
The game will randomly select a word from the list of words and provide a set of blank spaces equivalent to the word.

The user is prompted to guess one letter at a time to figure out the word.

If the user guesses correctly, the game will tell them how many unique letters are left to guess and prompt them to guess again.

If the user guesses incorrectly, the game will tell them this, show how many lives they have remaining and then prompt them to guess again.

If an invalid guess is entered the game will tell the user and prompt them to guess again.

If a previous guess is repeated, the game will tell the user, list their previous guesses and prompt them to guess again.


The user must guess the word before they run out of lives to win the game.

If the user runs out of lives they lose the game. 

A short list of example words are inlcuded in 'Hangman_Game.py' as the variable 'word_list'.

This can be updated with your own list of words.

## File structure of the project
The entire game is contained within the 'Hangman_Game.py' file.

## License information
This game is licenced under the MIT Licence as outlined below.

MIT License

Copyright (c) 2024 Claire Castanheira

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
