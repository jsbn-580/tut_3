import tkinter as tk

low = 1
high = 100
guess = (low + high) // 2

def too_small():
    global low, guess
    low = guess + 1
    update()

def too_large():
    global high, guess
    high = guess - 1
    update()

def correct():
    label.config(text=f"Correct! It was {guess}")
    disable_buttons()

def update():
    global guess
    guess = (low + high) // 2
    label.config(text=f"Computer guesses: {guess}")

def disable_buttons():
    b1.config(state=tk.DISABLED)
    b2.config(state=tk.DISABLED)
    b3.config(state=tk.DISABLED)

def new_game():
    global low, high
    low, high = 1, 100
    update()
    b1.config(state=tk.NORMAL)
    b2.config(state=tk.NORMAL)
    b3.config(state=tk.NORMAL)

root = tk.Tk()
label = tk.Label(root, text=f"Computer guesses: {guess}")
label.pack()

b1 = tk.Button(root, text="Too Small", command=too_small)
b1.pack()
b2 = tk.Button(root, text="Too Large", command=too_large)
b2.pack()
b3 = tk.Button(root, text="Correct", command=correct)
b3.pack()
tk.Button(root, text="New Game", command=new_game).pack()
root.mainloop()
