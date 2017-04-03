"""Create Animal class
Every animal has a hunger value, which is a whole number
Every animal has a thirst value, which is a whole number
when creating a new animal object these values are created with the default 50 value
Every animal can eat() which decreases their hunger by one
Every animal can drink() which decreases their thirst by one
Every animal can play() which increases both by one"""

class Animal():
    def __init__(self):
        self.hunger = 50
        self.thirst = 50

    def eating(self):
        self.hunger -= 1

    def drinking(self):
        self.thirst -= 1

    def playing(self):
        self.hunger += 1
        self.thirst += 1

cockroach = Animal()

cockroach.eating()
cockroach.drinking()
cockroach.eating()
cockroach.eating()
cockroach.drinking()
cockroach.playing()

print(cockroach.hunger, cockroach.thirst)
