class Apples:
    def __init__(self, apple = "apple"):
        self.apple = apple

    def get_apple(self):
        return self.apple

class Sum_stuff:
    def __init__(self, list_of_numbers = []):
        self.list_of_numbers = list_of_numbers

    def sum_all(self):
        numbers = 0
        for n in self.list_of_numbers:
            numbers += n
        if numbers == 0:
            return 0
        else:
            return numbers

class Anagram:
    def __init__(self, string1 = "", string2 = ""):
        self.string1 = string1
        self.string2 = string2

    def anagrams(self):
        if "".join(sorted(self.string1)) == "".join(sorted(self.string2)):
            return True
        else:
            return False

class LetterCounter:
    def __init__(self, string):
        self.string = string

    def count_letters(self):
        dic = {}
        for letter in self.string:
            if letter not in dic:
                dic[letter] = 1
            else:
                dic[letter] += 1
        return dic

class Fibonacci:
    def __init__(self, numbers):
        self.numbers = numbers

    def fibonacci(self, numbers):
        self.numbers = numbers
        if self.numbers < 2:
            return numbers
        else:
            return self.fibonacci(numbers -1) + self.fibonacci(numbers -2)
