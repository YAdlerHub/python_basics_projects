import tkinter as tk
from tkinter import messagebox
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("400x500")
        
        self.expression = ""  # Stores the current mathematical expression
        
        # Entry widget to display expressions
        self.entry = tk.Entry(root, font=("Arial", 18), bd=10, relief=tk.RIDGE, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, padx=10, pady=10)

        # Button layout
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("%", 4, 2), ("+", 4, 3),
            ("(", 5, 0), (")", 5, 1), ("√", 5, 2), ("^", 5, 3),
            ("C", 6, 0), ("=", 6, 1, 3)
        ]

        # Creating buttons
        for button in buttons:
            text = button[0]
            row = button[1]
            col = button[2]
            colspan = button[3] if len(button) > 3 else 1
            self.create_button(text, row, col, colspan)

    def create_button(self, text, row, col, colspan=1):
        """Create calculator buttons."""
        button = tk.Button(
            self.root, text=text, font=("Arial", 16), width=5, height=2,
            command=lambda: self.on_button_click(text)
        )
        button.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew")

    def on_button_click(self, char):
        """Handles button click events."""
        if char == "=":
            self.calculate_result()
        elif char == "C":
            self.expression = ""
            self.update_entry()
        elif char == "√":
            self.expression += "math.sqrt("
            self.update_entry()
        elif char == "^":
            self.expression += "**"
            self.update_entry()
        else:
            self.expression += char
            self.update_entry()

    def update_entry(self):
        """Updates the entry field with the current expression."""
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def calculate_result(self):
        """Evaluates the mathematical expression."""
        try:
            result = eval(self.expression, {"math": math, "__builtins__": {}})
            self.expression = str(result)
            self.update_entry()
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            self.expression = ""
            self.update_entry()

# Run the calculator
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
