
a = input("I want to play a game. Gimme a word! - ")
b = input("I need another one to play with! I will tell you if they are anagrams. - ")

def anagram(a, b):
    for l in b:
        if l not in a:
            return False
        else:
            return True
    for l in a:
        if l not in b:
            return False
        else:
            return True
print(anagram(a, b))
