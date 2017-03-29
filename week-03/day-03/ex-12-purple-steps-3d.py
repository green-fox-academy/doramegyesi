# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/exercises/drawing/purple-steps-3d/r4.png]

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

s = 0
def drawing(size):
    square = canvas.create_rectangle(s, s, s*2, s*2, fill = "mediumorchid")
    return square

for n in range(6):
    s = 2*s
    drawing(s)*n

root.mainloop()
