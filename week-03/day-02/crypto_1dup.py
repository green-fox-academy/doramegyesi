# Create a method that decrypts the texts/duplicated_chars.txt

text = open("duplicated_charts.txt", "r")
fw = text.read()
text.close()

def decrypt(fw):
        print(fw[::2])

decrypt(fw)
