class Garden():
    flowers = []
    trees = []

    def print_status(self):
        for n in self.flowers:
            if n[1] < 5:
                print("the", n[0], "flower needs water")
            else:
                print("the", n[0], "flower does not need water")
        for n in self.trees:
            if n[1] < 10:
                print("the", n[0], "tree needs water")
            else:
                print("the", n[0], "tree does not need water")

class Flower(Garden):
    def __init__(self, color, water_level = 0):
        self.color = color
        self.water_level = water_level
        self.flowers.append([self.color, self.water_level])

class Tree(Garden):
    def __init__(self, color, water_level = 0):
        self.color = color
        self.water_level = water_level
        self.trees.append([self.color, self.water_level])

flower_one =  Flower("yellow")
flower_two = Flower("blue", 10)
tree_one = Tree("purple")
tree_two = Tree("orange", 15)
Garden.print_status(Garden)
