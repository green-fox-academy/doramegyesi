# Create a method that decrypts texts/reversed_zen_lines.txt

text = open("reversed_lines.txt", "r")
stuff = text.read()
text.close()

def decrypt(stuff):
    print(stuff[::-1])

decrypt(stuff)
