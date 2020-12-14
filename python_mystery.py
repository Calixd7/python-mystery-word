import random
import string
file = open ('words.txt')
text = file.read().split()

easy_list = [ word.upper() for word in text if 4 <= len(word) <= 6 ]
normal_list = [ word.upper() for word in text if 6 <= len(word) <= 8]  
hard_list = [ word.upper()for word in text if 8 <= len(word)   ]
def get_level():
    level = input('Please select a level (easy, normal, hard):')
    if level == 'easy':
        word = random.choice(easy_list)
    elif level == 'normal':
        word = random.choice(normal_list)
    elif level == 'hard':
        word = random.choice(hard_list)
    else:
        return get_level()
    print(f'Your word is {len(word)} characters long.')
    return word
def display_word(word, guess_list):
    return [letter if letter in guess_list else '_' for letter in word]

def get_guess_list(guess_list):
    guess = input('Guess a letter:').upper()
    if len(guess) != 1:
        print('Please guess only one letter')
    else:
        guess_list.append(guess)
    return guess_list
def wrong_guess(word, guess_list):
    return sorted(set(
        letter
        for letter in guess_list
        if not letter in word
    ))
def game_play(word):
    guess_list = []
    while True:
        guesses_remaining = 8 - len(wrong_guess(word, guess_list))
        print(f"Incorrect letters: {' '.join(wrong_guess(word, guess_list))}")
        print(f"Mystery Word: {' '.join(display_word(word, guess_list))}")
        print(f"You have {guesses_remaining} guesses remaining.")
        if "_" not in display_word(word, guess_list):
            print(f'Congrats! You\'ve won! Your word was {word}\n')
            return
        if guesses_remaining == 0:
            print(f'You\'re out of guesses, Your word was {word}\n')
            return
        guess_list = get_guess_list(guess_list)

if __name__ == "__main__":
    word = (get_level())
    game_play(word)


