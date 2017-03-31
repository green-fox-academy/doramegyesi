from tkinter import *

root = Tk()

canvas = Canvas(root, width='600', height='600', bg="white")
canvas.pack()
def draw_circle(x, y, size):
    canvas.create_oval(x, y, x+size, y+size)

def rec_circle(x, y, size):
    draw_circle(x, y, size)
    canvas.update()
    if size > 38:
        rec_circle(x+1/4*size, y, size/2)
        rec_circle(x+2/60*size, y+3/8*size, size/2)
        rec_circle(x+28/60*size, y+3/8*size, size/2)


rec_circle(2, 2, 590)

root.mainloop()
