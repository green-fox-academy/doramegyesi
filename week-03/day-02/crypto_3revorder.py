text = open("reversed_order.txt", "r")
stuff = text.readlines()
text.close()

def decrypt(stuff):
    print(stuff[::-1])

decrypt(stuff)
