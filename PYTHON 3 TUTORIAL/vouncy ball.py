import tkinter as tk

def calculate():
    h = float(entry1.get())
    b = float(entry2.get())
    n = int(entry3.get())
    distance = h
    for _ in range(1, n):
        h *= b
        distance += 2 * h
    result.config(text=f"Total Distance: {round(distance, 2)}")

root = tk.Tk()
tk.Label(root, text="Initial Height").pack()
entry1 = tk.Entry(root)
entry1.pack()
tk.Label(root, text="Bounciness Index").pack()
entry2 = tk.Entry(root)
entry2.pack()
tk.Label(root, text="Number of Bounces").pack()
entry3 = tk.Entry(root)
entry3.pack()
tk.Button(root, text="Calculate", command=calculate).pack()
result = tk.Label(root, text="")
result.pack()
root.mainloop()
