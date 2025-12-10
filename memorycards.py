import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title('Memory')

# Skapa 6 par (12 kort)
cards = list(range(1, 7)) * 2
random.shuffle(cards)

buttons = []
flipped = []
matched = []

def press(i):
    if i in matched or i in [x[0] for x in flipped]:
        return

    # Visa kortet med markerad border
    buttons[i]['text'] = str(cards[i])
    buttons[i]['fg'] = '#741A12'
    buttons[i]['highlightbackground'] = '#891106'
    buttons[i]['highlightthickness'] = 5
    flipped.append((i, cards[i]))

    if len(flipped) == 2:
        root.after(500, check_match)

def check_match():
    global flipped

    if flipped[0][1] == flipped[1][1]:
        # När användare matchar kort
        for idx, _ in flipped:
            buttons[idx]['bg'] = '#5C9E53'
            buttons[idx]['highlightbackground'] = '#5C9E53'
            buttons[idx]['highlightthickness'] = 5
            matched.append(idx)
        if len(matched) == 12:
            messagebox.showinfo('Memory', 'Du har segrat!')
    else:
        # När användare inte hittar par
        for idx, _ in flipped:
            buttons[idx]['text'] = '?'
            buttons[idx]['fg'] = '#DAAAA6'
            buttons[idx]['highlightbackground'] = '#630A0A' 
            buttons[idx]['highlightthickness'] = 2
    flipped = []

# Skapa knappar med standardfärger
for i in range(12):
    btn = tk.Button(root, text='?', width=6, height=3,
                    fg='#DAAAA6',
                    bg='#630A0A',
                    font=('Arial', 20),
                    highlightthickness=2,
                    highlightbackground='#630A0A',
                    bd=2, relief='raised',
                    command=lambda i=i: press(i))
    btn.grid(row=i//4, column=i%4, padx=10, pady=10)
    buttons.append(btn)

root.mainloop()
