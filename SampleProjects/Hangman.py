import random
from words import words
import string

# print(words[len(words)-1])

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    random_word = get_valid_word(words)
    # print random_word
    random_word_letters = set(random_word) #set of words in random word
    alphabet = set(string.ascii_uppercase) #set of alphabets
    used_letters = set() #what user has guessed already

    while len(random_word_letters) > 0:
        print('You have used the letters ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in random_word]
        print('Current word: ', ''.join(word_list))
        user_letter = input('Guess a letter......: ').upper()
        unused_letters = alphabet - used_letters
        if user_letter in unused_letters:
            used_letters.add(user_letter)
            if user_letter in random_word_letters:
                random_word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print('You have already used that letter')
        else:
            print('Invalid character')
    return word_list


print(hangman())
