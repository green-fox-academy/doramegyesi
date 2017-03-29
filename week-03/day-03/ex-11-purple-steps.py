# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/exercises/drawing/purple-steps/r3.png]

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

s = 0

def drawing(size):
    square = canvas.create_rectangle(s, s, s+10, s+10, fill = "mediumorchid")
    return square

for n in range(20):
    s += 10
    drawing(s)*n

root.mainloop()
