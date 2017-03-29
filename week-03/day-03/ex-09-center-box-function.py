# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def drawing(s):
    x = 150
    y = 150
    square = canvas.create_rectangle(x - s/2, y - s/2, x + s/2, y + s/2)

drawing(200)
drawing(80)
drawing(20)

root.mainloop()
