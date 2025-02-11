import random

# Load words from file
def load_words(filename="words.txt"):
    try:
        with open(filename, "r") as file:
            words = [word.strip().lower() for word in file.readlines() if len(word.strip()) == 5]
        return words if words else ["apple"]  # Default word if file is empty
    except FileNotFoundError:
        return ["apple"]  # Default word if file is missing

# Function to check and display guess feedback
def check_guess(secret_word, guess):
    feedback = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            feedback.append("✅")  # Correct letter and position
        elif guess[i] in secret_word:
            feedback.append("🟡")  # Correct letter, wrong position
        else:
            feedback.append("⬜")  # Letter not in the word
    return " ".join(feedback)

# Wordle game function
def wordle():
    words = load_words()
    secret_word = random.choice(words)
    attempts = 6

    print("🎮 Welcome to Wordle!")
    print("🔤 Try to guess a 5-letter word. You have 6 attempts.")

    while attempts > 0:
        guess = input("\n➡️ Enter your guess: ").strip().lower()

        if len(guess) != 5 or not guess.isalpha():
            print("❌ Invalid input! Please enter a 5-letter word.")
            continue

        attempts -= 1
        feedback = check_guess(secret_word, guess)
        print(f"📝 Feedback: {feedback}")

        if guess == secret_word:
            print(f"🎉 Congratulations! You guessed the word: {secret_word}")
            break

        print(f"❤️ Attempts left: {attempts}")

    else:
        print(f"☠️ Game over! The correct word was: {secret_word}")

# Run the game
if __name__ == "__main__":
    wordle()
