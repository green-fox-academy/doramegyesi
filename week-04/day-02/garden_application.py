class Garden:
    def __init__(self):
        self.flowers = []
        self.trees = []

    def watering(self, watering):
        pass

    def print_status(self):
        pass

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
flower_two = Flower("blue")
tree_one = Tree("purple")
tree_two = Tree("orange")
