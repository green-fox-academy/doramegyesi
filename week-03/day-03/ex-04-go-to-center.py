# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

z = (150, 150)
def drawing(x, y, z):
    line = canvas.create_line(x, y, z)

drawing(0, 0, z)
drawing(300, 0, z)
drawing( 150, 300, z)

root.mainloop()
