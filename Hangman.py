import random
import string
from words_list import words, cars_words, animals_words, math_words


def get_category(word_cat):
    while True:
        player_choice = input('choose a word category, use A (Animals), C (Cars), M (Math), R (Random): ')\
            .strip().lower()
        if player_choice == 'a':
            word_cat = animals_words
            break
        if player_choice == 'c':
            word_cat = cars_words
            break
        if player_choice == 'm':
            word_cat = math_words
            break
        if player_choice == 'r':
            word_cat = words
            break
        else:
            print(f'{player_choice} is not a valid option, please try again')
            continue
    return word_cat


def get_valid_word(word):
    word = random.choice(get_category(word_cat=word))
    while '-' in word or ' ' in word:
        random.choice(get_category(word_cat=word))
    return word


def hangman():
    word = get_valid_word(word=True)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_lowercase)
    used_letters = set()  # what the user has guessed

    lives = 6

    # getting the input from the user
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print(f'you have {lives} lives left and you have used these letters: ', ' '.join(used_letters))

        # what the current word is (W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            # removes the letter the user has guessed
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1  # lose a life if the player guesses wrong
                print('Sorry, this letter is not part of the word.')

        elif user_letter in used_letters:
            print('You have already used that letter. Please try again.')

        else:
            print('Character is invalid. Please try again')

    #  player wins or loses messages
    if lives == 0:
        print(f'You have lost! The word was {word}')
    else:
        print(f'Congrats you have guessed the word {word}')


hangman()
