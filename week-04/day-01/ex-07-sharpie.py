"""Create Sharpie class
We should know about each sharpie their color (which should be a string),
width (which will be a floating point number), ink_amount (another floating point number)
When creating one, we need to specify the color and the width
Every sharpie is created with a default 100 as ink_amount
We can use() the sharpie objects which decreases inkAmount"""

class Sharpie():
    def __init__(self, color = "black", width = 0):
        self.inkAmount = 100
        self.color = color
        self.width = width

    def use(self, amount = 10):
        self.inkAmount -= amount
        return self.inkAmount

sharpie1 = Sharpie("yellow", 8.25)
sharpie2 = Sharpie("red")

print(sharpie1.color, sharpie1.width)

print(sharpie2.color, sharpie2.width)

sharpie1.use()

print(sharpie1.inkAmount)

sharpie2.use(35)

print(sharpie2.inkAmount)
