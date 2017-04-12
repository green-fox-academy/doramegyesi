from tkinter import *

root = Tk()

canvas = Canvas(root, width = 720, height = 720, background = "black")
canvas.pack()

map_1 = [
	[0,0,1,0,0,1,0,0,1,0],
	[0,1,1,0,1,1,0,0,0,0],
	[0,1,0,0,0,1,1,1,0,0],
	[0,0,0,0,0,0,1,0,0,0],
	[1,1,1,0,0,0,1,0,0,0],
	[0,0,1,0,0,0,0,0,0,1],
	[0,0,1,0,1,0,1,1,1,0],
    [0,0,0,0,1,0,0,1,1,0],
    [0,1,1,0,1,1,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0]
]

class FieldMap():
    def __init__(self):
        self.img_floor = PhotoImage(file = "floor.png")
        self.img_wall = PhotoImage(file = "wall.png")

    def draw_map(self):
        tile = 72
        for row in range(len(map_1)):
            for column in range (len(map_1[row])):
                if map_1[row][column] == 0:
                    canvas.create_image(row*tile, column*tile, anchor = NW, image = self.img_floor)
                else:
                    canvas.create_image(row*tile, column*tile, anchor = NW, image = self.img_wall)

class Characters():
    def __init__(self):
        self.img_hero_up = PhotoImage(file = "hero-up.png")
        self.img_hero_down = PhotoImage(file = "hero-down.png")
        self.img_hero_left = PhotoImage(file = "hero-left.png")
        self.img_hero_right = PhotoImage(file = "hero-right.png")
        self.img_boss = PhotoImage(file = "boss.png")
        self.img_skeleton = PhotoImage(file = "skeleton.png")
        self.position_x = 0
        self.position_y = 0

    def draw_hero(self, x, y):
        canvas.create_image(x, y, anchor = NW, image = self.img_hero_down)

field = FieldMap()
field.draw_map()
hero = Characters()
hero.draw_hero(0,0)

root.mainloop()
