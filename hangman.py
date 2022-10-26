import random
from words import words
from manimg import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses word from list
    while '-' in word or ' ' in word:
        word = random.choice(words)  # keeps word until guessed

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)  # sets letters of alphabet
    used_letters = set()  # guessed letters

    lives = 7

    # user input
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives and you have used : ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()  # make everything upper to match words
        if user_letter in alphabet - used_letters:   # if is in alphabet and not in used letters add to used letters
            used_letters.add(user_letter)
            if user_letter in word_letters:  # if guessed letter in word remove letter from remaining letters to guess
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, Congratulations. The word was', word)
    else:
        print('WOOOOT! You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()