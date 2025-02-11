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

# Check guess and return colored feedback
def check_guess(secret_word, guess):
    feedback = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            feedback.append(("green", guess[i]))  # ✅ Correct letter & position
        elif guess[i] in secret_word:
            feedback.append(("yellow", guess[i]))  # 🟡 Correct letter, wrong position
        else:
            feedback.append(("gray", "_"))  # ⬜ Letter not in the word
    return feedback

# Wordle game with UI
class WordleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordle Game")
        self.root.geometry("400x550")
        self.words = load_words()

        # Select category
        self.category_label = tk.Label(root, text="Choose a category:", font=("Arial", 12))
        self.category_label.pack(pady=5)

        self.category_var = tk.StringVar(value="animals")
        self.category_menu = tk.OptionMenu(root, self.category_var, *self.words.keys())
        self.category_menu.pack(pady=5)

        self.start_button = tk.Button(root, text="Start Game", font=("Arial", 12), command=self.start_game)
        self.start_button.pack(pady=10)

        # Game UI
        self.word_frame = tk.Frame(root)
        self.word_frame.pack(pady=10)

        self.guess_entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.guess_entry.pack(pady=10)
        self.guess_entry.bind("<Return>", self.make_guess)

        self.keyboard_frame = tk.Frame(root)
        self.keyboard_frame.pack(pady=10)

        self.attempts_label = tk.Label(root, text="", font=("Arial", 12))
        self.attempts_label.pack(pady=5)

        self.feedback_labels = []
        self.secret_word = ""
        self.attempts = 6
        self.guessed_letters = set()

    def start_game(self):
        """Start a new game with a random word from the chosen category."""
        category = self.category_var.get()
        self.secret_word = random.choice(self.words[category])
        self.attempts = 6
        self.guessed_letters.clear()

        self.feedback_labels = []
        for widget in self.word_frame.winfo_children():
            widget.destroy()

        for _ in range(len(self.secret_word)):
            lbl = tk.Label(self.word_frame, text="_", font=("Arial", 20), width=3)
            lbl.pack(side=tk.LEFT, padx=5)
            self.feedback_labels.append(lbl)

        self.create_keyboard()
        self.attempts_label.config(text=f"Attempts left: {self.attempts}")

    def create_keyboard(self):
        """Create a keyboard with colored buttons."""
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
        """Check the guess and update UI with colored feedback."""
        guess = self.guess_entry.get().strip().lower()
        if len(guess) != len(self.secret_word) or not guess.isalpha():
            self.attempts_label.config(text="❌ Invalid guess! Enter a valid word.", fg="red")
            return

        self.attempts -= 1
        feedback = check_guess(self.secret_word, guess)

        for i, (color, letter) in enumerate(feedback):
            self.feedback_labels[i].config(text=letter.upper(), fg=color)

        if guess == self.secret_word:
            self.attempts_label.config(text="🎉 You Won!", fg="green")
            return

        if self.attempts == 0:
            self.attempts_label.config(text=f"☠️ Game Over! The word was: {self.secret_word.upper()}", fg="red")

        self.guess_entry.delete(0, tk.END)

# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    game = WordleGame(root)
    root.mainloop()
