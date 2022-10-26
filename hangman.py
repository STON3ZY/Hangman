# Hangman
# Need a list of words (import)
#
#
#
#
#
#
#
#
#
#
#
#
#

import random
import string

from words import words


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses word from list
    while '-' in word or ' ' in word:
        word = random.choice(words)  # keeps word until guessed

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)   # letters in words
    alphabet = set(string.ascii_uppercase)  # sets letters of alphabet
    used_letters = set()  # guessed letters

    # user inputs
    while len(word_letters) > 0:
        print('You have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()  # make everything upper to match words
        if user_letter in alphabet - used_letters:  # if is in alphabet and not in used letters add to used letters
            used_letters.add(user_letter)
            if user_letter in word_letters:  # if guessed letter in word remove letter from remaining letters to guess
                word_letters.remove(user_letter)
                print('')

        elif user_letter in used_letters:
            print('You have tried this letter already. Please try again!')

        else:
            print("I didn't understand that. Please try again")

        if len(word_letters) == 0:
            print('Woot! you got it!!! ', word)


if __name__ == '__main__':
    hangman()