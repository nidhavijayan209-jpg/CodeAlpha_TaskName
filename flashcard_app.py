import tkinter as tk
from tkinter import simpledialog, messagebox

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Quiz App")

        self.flashcards = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "What is 2 + 2?", "answer": "4"},
            {"question": "What is the color of the sky?", "answer": "Blue"},
        ]
        self.current = 0
        self.showing_answer = False

        self.question_label = tk.Label(root, text="", font=('Arial', 18), wraplength=400)
        self.question_label.pack(pady=20)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Previous", command=self.prev_card).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Show Answer", command=self.toggle_answer).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Next", command=self.next_card).pack(side=tk.LEFT, padx=5)

        action_frame = tk.Frame(root)
        action_frame.pack(pady=10)

        tk.Button(action_frame, text="Add", command=self.add_card).pack(side=tk.LEFT, padx=5)
        tk.Button(action_frame, text="Edit", command=self.edit_card).pack(side=tk.LEFT, padx=5)
        tk.Button(action_frame, text="Delete", command=self.delete_card).pack(side=tk.LEFT, padx=5)

        self.update_card()

    def update_card(self):
        self.showing_answer = False
        if self.flashcards:
            self.question_label.config(text=self.flashcards[self.current]["question"])
        else:
            self.question_label.config(text="No flashcards available.")

    def toggle_answer(self):
        if not self.flashcards:
            return
        self.showing_answer = not self.showing_answer
        card = self.flashcards[self.current]
        self.question_label.config(text=card["answer"] if self.showing_answer else card["question"])

    def next_card(self):
        if self.flashcards:
            self.current = (self.current + 1) % len(self.flashcards)
            self.update_card()

    def prev_card(self):
        if self.flashcards:
            self.current = (self.current - 1) % len(self.flashcards)
            self.update_card()

    def add_card(self):
        q = simpledialog.askstring("Add Flashcard", "Enter question:")
        a = simpledialog.askstring("Add Flashcard", "Enter answer:")
        if q and a:
            self.flashcards.append({"question": q, "answer": a})
            self.current = len(self.flashcards) - 1
            self.update_card()

    def edit_card(self):
        if not self.flashcards:
            return
        card = self.flashcards[self.current]
        q = simpledialog.askstring("Edit Flashcard", "Edit question:", initialvalue=card["question"])
        a = simpledialog.askstring("Edit Flashcard", "Edit answer:", initialvalue=card["answer"])
        if q and a:
            self.flashcards[self.current] = {"question": q, "answer": a}
            self.update_card()

    def delete_card(self):
        if not self.flashcards:
            return
        confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this flashcard?")
        if confirm:
            self.flashcards.pop(self.current)
            self.current = max(0, self.current - 1)
            self.update_card()


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
