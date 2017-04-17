class Garden:
    def __init__(self):
        self.flowers = []
        self.trees = []

    def watering(self, watering):
        pass

class Flower(Garden):
    def __init__(self, color = "black", water_level = 0):
        self.color = color
        self.water_level = water_level

class Tree(Garden):
    def __init__(self, color = "black"):
        self.color = color
