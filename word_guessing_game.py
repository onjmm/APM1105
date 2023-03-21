#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random

# Function to read the words from the file and return a random word
def random_word():
    with open(r'words.txt', 'r') as file:
        wordsList = file.read().split()
    return random.choice(wordsList).strip()

# Function to display the current state of the word
def display_word(wordsList, guessed_letters):
    displayed_word = ''
    for letter in wordsList:
        if letter in guessed_letters:
            displayed_word += letter + ' '
        else:
            displayed_word += '_ '
    return displayed_word.strip()

# Function to get the player's guess
def get_guess():
    while True:
        guess = input('Guess a letter: ').lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print('Invalid input. Please enter a single letter.')

# Main function to run the game
def main():
    print('Welcome to the word guessing game!')
    wordwList = get_word()
    max_guesses = 8
    guessed_letters = set()
    while max_guesses > 0:
        print(f'Word: {display_word(wordsList, guessed_letters)}')
        print(f'Guesses left: {max_guesses}')
        guess = get_guess()
        if guess in guessed_letters:
            print('You already guessed that letter. Please try again.')
        elif guess in wordsList:
            guessed_letters.add(guess)
            if set(wordsList) == guessed_letters:
                print(f'Congratulations, you guessed the word {wordsList}!')
                return
        else:
            guessed_letters.add(guess)
            max_guesses -= 1
    print(f'Sorry, you ran out of guesses. The word was {wordsList}.')


# In[ ]:




