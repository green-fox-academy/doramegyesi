# write a function that takes a filename and returns the number of lines the
# file contains. It should return zero if the file does not exist.

text = open("reversed_lines.txt", "r")
t = text.readlines()
text.close()

def total_lines(t):
    for lines in range(len(t)):
        lines += 1
    print(lines)

total_lines(t)
