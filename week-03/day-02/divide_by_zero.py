# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0

b = int(input("Give me a number! "))

def take_it(b):
    try:
        c = 10/b
        print(c)
    except ZeroDivisionError:
        print("fail")

take_it(b)
