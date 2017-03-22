# - Write a function called `sum` that sum all the numbers
#   until the given parameter

def sum(*args):
    total = 0
    for num in args:
        total += num
    print(total)


sum(1, 2, 3, 4)
