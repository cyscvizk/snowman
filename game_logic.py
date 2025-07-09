# game_logic.py

import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]
MAX_TRIES = len(STAGES) - 1  # 3 allowed mistakes

def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the snowman stage and word progress."""
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word.strip())
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print("\n")

def play_game():
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    while mistakes < MAX_TRIES:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❗ Please enter a single alphabetic character.")
            continue
        if guess in guessed_letters:
            print("⚠️ You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            if all(letter in guessed_letters for letter in secret_word):
                display_game_state(mistakes, secret_word, guessed_letters)
                print("🎉 You saved the snowman! The word was:", secret_word)
                return
        else:
            mistakes += 1
            print(f"❌ Wrong guess! Mistakes: {mistakes}/{MAX_TRIES}")

    # Game over
    display_game_state(mistakes, secret_word, guessed_letters)
    print("💀 The snowman has melted! The word was:", secret_word)
