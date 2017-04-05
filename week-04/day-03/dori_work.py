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
        if numbers ==0:
            return []
        else:
            return numbers
