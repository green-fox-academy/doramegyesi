from tkinter import *

root = Tk()

canvas = Canvas(root, width = 720, height = 720, background = "black")
canvas.pack()

map = [
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

class Tile():
    def __init__(self):
        self.img_floor = PhotoImage(file = "floor.png")
        self.img_wall = PhotoImage(file = "wall.png")
        self.img_hero_up = PhotoImage(file = "hero-up.png")
        self.img_hero_down = PhotoImage(file = "hero-down.png")
        self.img_hero_left = PhotoImage(file = "hero-left.png")
        self.img_hero_right = PhotoImage(file = "hero-right.png")
        self.img_boss = PhotoImage(file = "boss.png")
        self.img_skeleton = PhotoImage(file = "skeleton.png")

    def draw(self):
        first_square = canvas.create_image(36, 36, image = self.img_floor)

floor = Tile()
floor.draw()

root.mainloop()
