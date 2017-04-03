class Thing:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def complete(self):
        self.completed = True
        return self.completed

    def __str__(self):
        return ("[x] " if self.completed else "[ ] ") + self.name
