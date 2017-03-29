# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

size = 300
color = ["red", "orange", "yellow", "springgreen", "skyblue", "royalblue"]

def drawing(size, color):
    sq = canvas.create_rectangle(150-size/2, 150-size/2, 150+size/2, 150+size/2, fill = color)
    return sq
    
for c in range(len(color)):
    drawing(size, color[c])
    size -= 50

root.mainloop()
