# Create a program that prints all the even numbers between 0 and 500
for a in range(0, 501, 2):
    if a == 0:
        a += 2
    else:
        print(a)
