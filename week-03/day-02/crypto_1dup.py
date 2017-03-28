# Create a method that decrypts the texts/duplicated_chars.txt

text = open("duplicated_charts.txt", "r")
fw = text.read()
text.close()

def decrypt(fw):
    print(fw[::2])

decrypt(fw)

# or:

def decrypt(fw):
    new_text = ""
    for l in range(0, len(fw), 2):
        new_text +=  fw[l]
    print(new_text)

decrypt(fw)
