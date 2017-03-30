
from tkinter import *

root = Tk()

canvas = Canvas(root, width='600', height='600')
canvas.pack()

def draw_square(x, y, size):
    canvas.create_rectangle(x, y, x+size, y+size, width=2, fill="yellow")

def recursive_something(x, y, size):
    draw_square(x, y, size)
    canvas.update()
    if size > 10:
        recursive_something(x+1/3*size, y, size/3)
        recursive_something(x+1/3*size, y+2/3*size, size/3)
        recursive_something(x, y+1/3*size, size/3)
        recursive_something(x+2/3*size, y+1/3*size, size/3)

recursive_something(5, 5, 590)

root.mainloop()
