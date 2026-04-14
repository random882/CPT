import random
import pygame
import time

MILLIS = 1000
MAX_VOLUME = 1
FADE_IN_MS = 3 * MILLIS
FADE_OUT_MS = 3 * MILLIS

hangman_parts = [
r"""
   
   
""",
r"""
  O 
   
""",
r"""
  O
  |   
""",
r"""
  O
  |\     
""",
r"""
  O
 /|\ 
""",
r"""
  O 
 /|\
   \
""",
r"""
  O
 /|\
 / \
 """
]
words = {
    "Houses": {
        "Hint": "People live in this.", 
        "Definition": "A structure that people live in."

    },
    "Mouses": {
        "Hint": "A small creature.", 
        "Definition": "A tiny rodent."

    },
"Computer": {
        "Hint": "A type of device seen in primarily two different forms.", 
        "Definition": "Form of technology used to store and searchup information."

    },
}
choices = list(words.keys())
bad_guesses = []
good_guesses = []
word_to_guess = random.choice(choices)
alphabet = "abcdefghijklmnopqrstuvwxyz"
def start_backgroundmusic():
    pygame.mixer.init()

    pygame.mixer.music.load(r"D:\coding\audio\Elevator.mp3")

    pygame.mixer.music.set_volume(MAX_VOLUME)

    pygame.mixer.music.play(-1,0,FADE_IN_MS)

def stop_music():
    pygame.mixer.music.fadeout(FADE_OUT_MS)
    time.sleep(FADE_OUT_MS / MILLIS)

def is_valid(guess):
    if len(guess) == 1 and guess in alphabet:
        return True
    else:
        print("Single letter only, try again.")
        return False

def already_guessed(guess):
    result = False
    if guess in good_guesses or guess in bad_guesses:
        print("Already guessed, try a different letter.")
        result = True
    else:
        if guess in word_to_guess.lower():
            good_guesses.append(guess)
        else:
            bad_guesses.append(guess)
    return result

def create_display_word():
    result = ""
    # to do: create the word
    for letter in word_to_guess:
        if letter.lower() in good_guesses:
            result = result + letter
        else:
            result = result + "_"
    return result

def display_gallows():
    print(hangman_parts[len(bad_guesses)])

def is_game_over(display_word):
    if hangman_parts[len(bad_guesses)] == hangman_parts[-1]:
        print(f"You have lost, the real word was {word_to_guess}")
        return True
    if display_word.lower() == word_to_guess.lower():
        print("You have won!")
        print(f"{word_to_guess}: {words[word_to_guess]["Definition"]}")
        return True

def main():
        

    start_backgroundmusic()

    print(f"Hint: {words[word_to_guess]["Hint"]}")

    while True:
        
        guess = input("Guess a letter. ").lower()
        # check that guess is always a letter.
        # check that guess is a single character
        if not is_valid(guess):
            continue
        # if it's already been guessed try again.
        if already_guessed(guess):
            continue
        display_gallows()
        display_word = create_display_word()
        print(display_word)
        if is_game_over(display_word):
            break

    stop_music()
if __name__=="__main__":
    main()