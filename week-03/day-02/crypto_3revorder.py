def decrypt(stuff):
    text = open(stuff, "r")
    stuff = text.readlines()
    text.close()
    print(stuff[::-1])

decrypt("reversed_order.txt")
