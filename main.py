
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики нолики до 3 побед")
window.geometry("400x450")

current_plaer = "X"
buttons = []
scorers = {"X": 0, "0": 0} #Счётчик побед

def on_click(row, col):
    pass



# Cоздание игрового поля
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2, command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j, padx=5, pady=5)
        row.append(btn)
    buttons.append(row)

window.mainloop()
