import random
import os
import time

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Predefined words list
WORDS = ["python", "galaxy", "planet", "rocket", "comet"]

# Main Hangman Game
def hangman():
    clear_screen()
    print("=" * 60)
    print("               🚀 HANGMAN: SPACE EDITION 🚀")
    print("=" * 60)
#Bhaskar Raj
    word = random.choice(WORDS)
    guessed = ['_'] * len(word)
    guessed_letters = []
    attempts_left = 6

    while attempts_left > 0 and ''.join(guessed) != word:
        print(f"\nWord: {' '.join(guessed)}")
        print(f"Guessed Letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        print(f"Attempts Left: {attempts_left}")

        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("⚠️ You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            attempts_left -= 1
            print("❌ Wrong guess!")

        time.sleep(1)
        clear_screen()
        print("=" * 60)
        print("               🚀 HANGMAN: SPACE EDITION 🚀")
        print("=" * 60)
#Bhaskar Raj
    # Final Result
    if ''.join(guessed) == word:
        print(f"\n🎉 Congratulations! You guessed the word: {word.upper()}")
    else:
        print(f"\n💀 Game Over! The word was: {word.upper()}")

    print("=" * 60)

# Run the game
if __name__ == "__main__":
    hangman()
