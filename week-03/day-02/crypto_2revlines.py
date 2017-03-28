# Create a method that decrypts texts/reversed_zen_lines.txt



def decrypt(thing):
    text = open(thing, "r")
    thing = text.readlines()
    text.close()
    new = ""
    for b in range(len(thing)):
        new += thing[b][::-1]
    print(new)

decrypt("reversed_lines.txt")
