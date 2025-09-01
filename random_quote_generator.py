import tkinter as tk
import random

# List of quotes (text, author)
quotes = [
    ("The greatest glory in living lies not in never falling, but in rising every time we fall.", "Nelson Mandela"),
    ("The way to get started is to quit talking and begin doing.", "Walt Disney"),
    ("Your time is limited, so don't waste it living someone else's life.", "Steve Jobs"),
    ("If life were predictable it would cease to be life, and be without flavor.", "Eleanor Roosevelt"),
    ("If you look at what you have in life, you'll always have more.", "Oprah Winfrey"),
    ("If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.", "James Cameron"),
    ("Life is what happens when you're busy making other plans.", "John Lennon")
]

# Function to display a new quote
def display_quote():
    quote, author = random.choice(quotes)
    quote_label.config(text=quote)
    author_label.config(text=f"- {author}")

# Create the main window
root = tk.Tk()
root.title("Random Quote Generator")
root.geometry("400x200")
root.configure(bg="white")

# Quote label
quote_label = tk.Label(root, text="", wraplength=350, justify="center", font=("Helvetica", 12), bg="white")
quote_label.pack(pady=20)

# Author label
author_label = tk.Label(root, text="", font=("Helvetica", 10, "italic"), bg="white")
author_label.pack()

# Button to get a new quote
new_quote_button = tk.Button(root, text="New Quote", command=display_quote, bg="blue", fg="white", font=("Helvetica", 12))
new_quote_button.pack(pady=20)

# Show the first quote
display_quote()

# Run the app
root.mainloop()