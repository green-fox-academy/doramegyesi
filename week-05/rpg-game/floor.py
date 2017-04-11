from tkinter import *

root = Tk()

canvas = Canvas(root, width = 720, height = 720, background = "black")
canvas.pack()

class Tile():
    def __init__(self):
        self.img_floor = PhotoImage(file = "floor.png")
        self.img_wall = PhotoImage(file = "wall.png")

    def draw(self):
        first_square = canvas.create_image(36, 36, image = self.img_floor)

floor = Tile()
floor.draw()

root.mainloop()
