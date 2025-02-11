import random

# Load words from file
def load_words(filename="words.txt"):
    try:
        with open(filename, "r") as file:
            words = file.read().splitlines()
        return words if words else ["python"]  # Default word if file is empty
    except FileNotFoundError:
        return ["python"]  # Default word if file is missing

# Display the current word progress
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Hangman game function
def hangman():
    words = load_words()
    secret_word = random.choice(words).lower()
    guessed_letters = set()
    attempts = 6

    print("🎮 Welcome to Hangman!")
    print(f"🔢 The word has {len(secret_word)} letters.")

    while attempts > 0:
        print("\n📌 Current word:", display_word(secret_word, guessed_letters))
        print(f"❤️ Attempts left: {attempts}")

        guess = input("➡️ Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input! Enter a single letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("✅ Correct guess!")
            if all(letter in guessed_letters for letter in secret_word):
                print(f"🎉 Congratulations! You guessed the word: {secret_word}")
                break
        else:
            attempts -= 1
            print("❌ Wrong guess!")

    else:
        print(f"☠️ Game over! The correct word was: {secret_word}")

# Run the game
if __name__ == "__main__":
    hangman()
