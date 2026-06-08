import tkinter as tk
import random

quotes = [
    {"text": "Seek knowledge, even if you have to go to China.", "author": "Prophet Muhammad SAWW"},
    {"text": "The best among you are those who have the best manners and character.", "author": "Prophet Muhammad SAWW"},
    {"text": "Kindness is a mark of faith, and whoever has not kindness has not faith.", "author": "Prophet Muhammad SAWW"},
    {"text": "Speak the truth even if it is bitter.", "author": "Prophet Muhammad SAWW"},
    {"text": "The ink of the scholar is more sacred than the blood of the martyr.", "author": "Prophet Muhammad SAWW"},
    {"text": "None of you truly believes until he loves for his brother what he loves for himself.", "author": "Prophet Muhammad SAWW"},
    {"text": "He who knows himself knows his Lord.", "author": "Hazrat Ali R.A"},
    {"text": "Do not use the sharpness of your speech on the mother who taught you how to speak.", "author": "Hazrat Ali R.A"},
    {"text": "Patience is of two kinds: patience over what pains you, and patience against what you covet.", "author": "Hazrat Ali R.A"},
    {"text": "The world is a prison for the believer and a paradise for the unbeliever.", "author": "Hazrat Ali R.A"},
    {"text": "Be like a flower that gives its fragrance even to the hand that crushes it.", "author": "Hazrat Ali R.A"},
    {"text": "Knowledge enlivens the soul.", "author": "Hazrat Ali R.A"},
    {"text": "Raise yourself so high that before every decree, God himself asks you: Tell me, what is your wish?", "author": "Allama Iqbal"},
    {"text": "The ultimate aim of the ego is not to see something, but to be something.", "author": "Allama Iqbal"},
    {"text": "Nations are born in the hearts of poets, they prosper and die in the hands of politicians.", "author": "Allama Iqbal"},
    {"text": "Work hard, be sincere, and serve your nation.", "author": "Quaid-e-Azam Muhammad Ali Jinnah"},
    {"text": "Think a hundred times before you take a decision, but once that decision is taken, stand by it as one man.", "author": "Quaid-e-Azam Muhammad Ali Jinnah"},
    {"text": "Failure is a word unknown to me.", "author": "Quaid-e-Azam Muhammad Ali Jinnah"},
    {"text": "Without education, man is as though in a closed room and with education he finds himself in a room with all its windows open.", "author": "Sir Syed Ahmad Khan"},
    {"text": "Educate yourself, for we are surrounded by enemies.", "author": "Sir Syed Ahmad Khan"},
]

def show_random_quote():
    q = random.choice(quotes)
    quote_label.config(text=f'"{q["text"]}"')
    author_label.config(text=f'— {q["author"]}')

# Window
window = tk.Tk()
window.title("Random Quote Generator")
window.geometry("600x400")
window.configure(bg="#1a1820")
window.resizable(False, False)

# Title
title = tk.Label(window, text="Daily Wisdom", font=("Georgia", 22, "bold"),
                 bg="#1a1820", fg="#c9a84c")
title.pack(pady=20)

# Quote Text
quote_label = tk.Label(window, text="", font=("Georgia", 13, "italic"),
                       bg="#1a1820", fg="#f0ece0", wraplength=500,
                       justify="center")
quote_label.pack(pady=30, padx=40)

# Author
author_label = tk.Label(window, text="", font=("Georgia", 11),
                        bg="#1a1820", fg="#c9a84c")
author_label.pack(pady=10)

# Button
btn = tk.Button(window, text="✦ New Quote", font=("Georgia", 12),
                bg="#c9a84c", fg="#1a1820", relief="flat",
                padx=20, pady=10, cursor="hand2",
                command=show_random_quote)
btn.pack(pady=30)

# Show first quote on start
show_random_quote()

window.mainloop()