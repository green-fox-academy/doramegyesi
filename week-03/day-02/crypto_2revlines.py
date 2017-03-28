# Create a method that decrypts texts/reversed_zen_lines.txt

text = open("reversed_lines.txt", "r")
thing = text.readlines()
text.close()

def decrypt(thing):
    new = ""
    for b in range(len(thing)):
        new += thing[b][::-1]
    print(new)

decrypt(thing)
