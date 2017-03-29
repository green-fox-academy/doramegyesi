# draw four different size and color rectangles.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

rect_01 = canvas.create_rectangle(20, 20, 40, 40, fill = "crimson")
rect_02 = canvas.create_rectangle(50, 40, 140, 100, fill = "silver")
rect_03 = canvas.create_rectangle(110, 150, 50, 130, fill = "indigo")
rect_04 = canvas.create_rectangle(250, 250, 170, 60, fill = "skyblue")

root.mainloop()
