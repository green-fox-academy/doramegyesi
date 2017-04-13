from tkinter import *

root = Tk()

canvas = Canvas(root, width = 720, height = 720, background = "black")

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

    def draw_hero(self, x, y, img):
        self.img = img
        canvas.create_image(x, y, anchor = NW, image = self.img_hero_up)
        canvas.create_image(x, y, anchor = NW, image = self.img_hero_down)
        canvas.create_image(x, y, anchor = NW, image = self.img_hero_right)
        canvas.create_image(x, y, anchor = NW, image = self.img_hero_left)

    def move_the_hero(self, e): #e = KeyPress
        if e.keycode == 38:
            self.position_y -= 72
            self.draw_hero(self.position_x, self.position_y, self.img_hero_up)
        elif e.keycode == 40:
            self.position_y += 72
            self.draw_hero(self.position_x, self.position_y, self.img_hero_down)
        elif e.keycode == 39:
            self.position_x += 72
            self.draw_hero(self.position_x, self.position_y, self.img_hero_right)
        elif e.keycode == 37:
            self.position_x -= 72
            self.draw_hero(self.position_x, self.position_y, self.img_hero_left)

field = FieldMap()
field.draw_map()
hero = Characters()
canvas.bind("<KeyPress>", hero.move_the_hero)
canvas.focus_set()
canvas.pack()

root.mainloop()
