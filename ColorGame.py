import random
from tkinter import *
window = Tk()
window.geometry("400x400")
txt = Entry(window)
txt.place(x = 120, y = 340)
score = 0
timeleft = 30
colours = ['Red', 'Blue', 'Green', 'Pink',' Black', 'Yellow', 'Orange', 'Purple', 'Magenta']


lbl = Label(window, text="Type in the colours of the words, and not the word text!", fg='black', font=('Times', 13))
lbl.place(x=10, y=10)
lbl1 = Label(window, text="Score : ", fg='black', font=('Times', 13))
lbl1.place(x=150, y=30)
lbl2 = Label(window, text="Time Left : ", fg='black', font=('Times', 13))
lbl2.place(x=150, y=50)
lbl3 = Label(window, fg=str(colours[1]), text=str(colours[0]), font=('Times', 93))
lbl3.place(x=50, y=70)

def StartGame(event):
    global timeleft
    if timeleft == 30:
        countdown()
    NextColour()

def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1
        lbl2.configure(text="Time Left : " + str(timeleft))
        lbl2.after(1000, countdown)

def NextColour():
    global score
    global timeleft
    if timeleft > 0:
        if txt.get().lower() == colours[1].lower():
            score += 1
        txt.delete(0, END)
        random.shuffle(colours)
        lbl3.config(fg=str(colours[1]), text=str(colours[0]))
        lbl1.config(text="Score: " + str(score))


window.bind('<Return>', StartGame)
window.mainloop()