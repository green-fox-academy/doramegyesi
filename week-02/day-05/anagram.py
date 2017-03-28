
a = input("I want to play a game. Gimme a word! - ")
b = input("I need another one to tell you if they are anagrams. - ")

def anagram(a, b):
    if len(a) == len(b):
        for l in b:
            if l not in a:
                return False
    else:
        return False
    return True
print(anagram(a, b))
