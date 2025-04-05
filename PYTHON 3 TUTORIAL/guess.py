import tkinter as tk
import random

secret = random.randint(1, 100)
guesses = 0

def check():
    global guesses
    guess = int(entry.get())
    guesses += 1
    if guess < secret:
        label.config(text="Too small, try again.")
    elif guess > secret:
        label.config(text="Too large, try again.")
    else:
        label.config(text=f"Correct! Total guesses: {guesses}")

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Guess", command=check).pack()
label = tk.Label(root, text="")
label.pack()
root.mainloop()
