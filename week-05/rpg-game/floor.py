from tkinter import *

root = Tk()

canvas = Canvas(root, width = 720, height = 720, background = "black")
canvas.pack()

map = [
	[0,0,1,0,0,1,0,0,0,0],
	[0,1,1,0,0,1,0,0,0,0],
	[0,1,0,0,0,1,1,1,0,0],
	[0,0,0,0,0,0,1,0,0,0],
	[0,1,1,0,0,0,1,0,0,0],
	[0,0,1,0,0,0,0,0,0,1],
	[0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,1,0,0,0,1,0],
    [0,1,0,0,1,1,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0]
]

class FieldMap():
    def __init___(self):
        #self.img_floor = PhotoImage(file = "floor.png")
        #self.img_wall = PhotoImage(file = "wall.png")

        def draw_map(self, map):
            tile = 72
            for row in range(len(map)):
                for column in range (len(map[row])):
                    if map[row][column] == 0:
                        canvas.create_image(row*tile, column*tile, anchor = nw, image = PhotoImage(file = "floor.png")
                    else:
                        canvas.create_image(row*tile, column*tile, anchor = nw, image = PhotoImage(file = "wall.png")

class Characters():
    def __init__(self):
        #self.img_floor = PhotoImage(file = "floor.png")
        #self.img_wall = PhotoImage(file = "wall.png")
        self.img_hero_up = PhotoImage(file = "hero-up.png")
        self.img_hero_down = PhotoImage(file = "hero-down.png")
        self.img_hero_left = PhotoImage(file = "hero-left.png")
        self.img_hero_right = PhotoImage(file = "hero-right.png")
        self.img_boss = PhotoImage(file = "boss.png")
        self.img_skeleton = PhotoImage(file = "skeleton.png")

field = FieldMap
field.draw_map(map)

root.mainloop()
