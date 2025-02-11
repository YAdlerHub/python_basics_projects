import tkinter as tk
import random
import json

# Load words from JSON file
def load_words(filename="words.json"):
    try:
        with open(filename, "r") as file:
            words = json.load(file)
        return words
    except (FileNotFoundError, json.JSONDecodeError):
        return {"default": ["apple", "grape", "house", "table", "mouse"]}

# Check the guess and return feedback
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

# Game logic
class WordleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordle Game")
        self.root.geometry("400x500")
        self.words = load_words()
        
        # Select category
        self.category_label = tk.Label(root, text="Choose a category:", font=("Arial", 12))
        self.category_label.pack(pady=5)
        
        self.category_var = tk.StringVar(value="animals")
        self.category_menu = tk.OptionMenu(root, self.category_var, *self.words.keys())
        self.category_menu.pack(pady=5)

        # Start game button
        self.start_button = tk.Button(root, text="Start Game", font=("Arial", 12), command=self.start_game)
        self.start_button.pack(pady=10)

        # Game screen (hidden initially)
        self.word_label = tk.Label(root, text="", font=("Arial", 16))
        self.word_label.pack(pady=10)

        self.guess_entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.guess_entry.pack(pady=10)
        self.guess_entry.bind("<Return>", self.make_guess)

        self.keyboard_frame = tk.Frame(root)
        self.keyboard_frame.pack(pady=10)

        self.feedback_label = tk.Label(root, text="", font=("Arial", 14))
        self.feedback_label.pack(pady=10)

        self.attempts_left = tk.Label(root, text="", font=("Arial", 12))
        self.attempts_left.pack(pady=5)

        self.reset_button = tk.Button(root, text="Restart", font=("Arial", 12), command=self.restart_game)
        self.reset_button.pack(pady=10)

        self.secret_word = ""
        self.attempts = 6
        self.guessed_letters = set()

    def start_game(self):
        """Start a new game by selecting a random word from the chosen category."""
        category = self.category_var.get()
        self.secret_word = random.choice(self.words[category])
        self.attempts = 6
        self.guessed_letters.clear()
        
        self.word_label.config(text="_ " * len(self.secret_word))
        self.feedback_label.config(text="")
        self.attempts_left.config(text=f"Attempts left: {self.attempts}")
        
        self.create_keyboard()

    def create_keyboard(self):
        """Create on-screen keyboard buttons."""
        for widget in self.keyboard_frame.winfo_children():
            widget.destroy()

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for letter in alphabet:
            button = tk.Button(self.keyboard_frame, text=letter, font=("Arial", 12),
                               width=3, command=lambda l=letter: self.add_letter(l))
            button.grid(row=alphabet.index(letter) // 9, column=alphabet.index(letter) % 9, padx=2, pady=2)

    def add_letter(self, letter):
        """Insert letter into the guess entry box."""
        current_text = self.guess_entry.get()
        if len(current_text) < len(self.secret_word):
            self.guess_entry.insert(tk.END, letter)

    def make_guess(self, event=None):
        """Check the guess and update UI."""
        guess = self.guess_entry.get().strip().lower()
        if len(guess) != len(self.secret_word) or not guess.isalpha():
            self.feedback_label.config(text="❌ Invalid guess! Enter a valid word.")
            return

        self.attempts -= 1
        feedback = check_guess(self.secret_word, guess)
        self.feedback_label.config(text=f"📝 {feedback}")
        self.attempts_left.config(text=f"Attempts left: {self.attempts}")

        if guess == self.secret_word:
            self.word_label.config(text=f"🎉 {self.secret_word.upper()} ✅")
            self.feedback_label.config(text="You won! 🎉")
            return

        if self.attempts == 0:
            self.word_label.config(text=f"☠️ The word was: {self.secret_word.upper()}")
            self.feedback_label.config(text="Game over!")

        self.guess_entry.delete(0, tk.END)

    def restart_game(self):
        """Restart the game by resetting everything."""
        self.start_game()

# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    game = WordleGame(root)
    root.mainloop()
