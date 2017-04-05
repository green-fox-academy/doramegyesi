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

    def anagram(self):
        if "".join(sorted(self.string1)) == "".join(sorted(self.string2):
            return True
        else:
            return False
