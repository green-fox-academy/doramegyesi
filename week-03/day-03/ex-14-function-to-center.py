# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

o = 150
x = 0
y = 0

def drawing(x, y):
    line = canvas.create_line(x, y, o, o)
    return line

for l in range(0, 301, 15):
    drawing(0, l)
    drawing(l, 0)
    drawing(300, l)
    drawing(l, 300)

root.mainloop()
