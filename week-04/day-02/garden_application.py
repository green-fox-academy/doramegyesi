class Garden():
    flowers = []
    trees = []

    def total_plants(self):
        total = 0
        for n in self.flowers:
            total += 1
        for n in self.trees:
            total += 1
        return total

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

    def watering_plants(self, water_amount):
        self.water_amount = water_amount
        divided_water_amount = water_amount / self.total_plants()
        for n in self.flowers:
            if n[1] < 5:
                n[1] += divided_water_amount * 0.75
        for n in self.trees:
            if n[1] < 10:
                n[1] += divided_water_amount * 0.4
        print("watering with", water_amount)

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

garden = Garden()
flower_one =  Flower("yellow")
flower_two = Flower("blue")
tree_one = Tree("purple")
tree_two = Tree("orange")
garden.print_status()
garden.watering_plants(40)
garden.print_status()
garden.watering_plants(70)
garden.print_status()
