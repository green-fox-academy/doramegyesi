# Create a method that decrypts texts/reversed_order.txt

def decrypt(stuff):
    text = open(stuff, "r")
    stuff = text.readlines()
    text.close()
    print(stuff[::-1])

decrypt("reversed_order.txt")


def decrypt(thing):
    text = open(thing, "r")
    thing = text.readlines()
    text.close()
    new = ""
    for b in thing[::-1]:
        new += b
    print(new)

decrypt("reversed_order.txt")
