from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.

line_1 = canvas.create_line(10, 10, 80, 10, fill = "blue")
line_2 = canvas.create_line(80, 10, 80, 90, fill = "orange")
line_3 = canvas.create_line(80, 90, 10, 90, fill = "red")
line_4 = canvas.create_line(10, 90, 10, 10, fill = "green")
root.mainloop()
