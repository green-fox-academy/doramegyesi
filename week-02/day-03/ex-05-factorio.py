# - Create a function called `factorio`
#   that returns it's input's factorial

def factorio(n):
    fact = 1
    for a in range(10):
        fact = fact * n
        print(fact)

factorio(2)
factorio(5)
factorio(11)
