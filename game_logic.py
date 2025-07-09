# game_logic.py

import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]
MAX_TRIES = len(STAGES) - 1

def get_random_word():
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])
    print("Word:", " ".join([letter if letter in guessed_letters else "_" for letter in secret_word]))
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print("-" * 40)

def get_valid_input(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("❗ Please enter a single alphabetic character.")
        elif guess in guessed_letters:
            print("⚠️ You've already guessed that letter.")
        else:
            return guess

def play_game():
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0

    print("🎮 Welcome to Snowman Meltdown!")

    while mistakes < MAX_TRIES:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = get_valid_input(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            if all(letter in guessed_letters for letter in secret_word):
                display_game_state(mistakes, secret_word, guessed_letters)
                print("🎉 You saved the snowman! The word was:", secret_word)
                return
        else:
            mistakes += 1
            print(f"❌ Nope! Mistake {mistakes} of {MAX_TRIES}.\n")

    display_game_state(mistakes, secret_word, guessed_letters)
    print("💀 The snowman has melted! The word was:", secret_word)

def ask_replay():
    while True:
        choice = input("\n🔁 Play again? (y/n): ").strip().lower()
        if choice in ('y', 'yes'):
            return True
        elif choice in ('n', 'no'):
            return False
        else:
            print("Please enter 'y' or 'n'.")
