# write a function that takes a filename and returns the number of lines the
# file contains. It should return zero if the file does not exist.



def total_lines(kutya):
    try:
        text = open(kutya, "r")
        t = text.readlines()
        text.close()
        for lines in range(len(t)):
            lines += 1
        print(lines)
    except FileNotFoundError:
        print("0")

total_lines("reversed_lines.txt")
