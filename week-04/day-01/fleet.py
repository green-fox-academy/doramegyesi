"""In the fleet_of_things file create a fleet
Achieve this output:
1. [ ] Get milk
2. [ ] Remove the obstacles
3. [x] Stand up
4. [x] Eat lunch"""

from thing import Thing

class Fleet(object):
    def __init__(self):
        self.things = []

    def add(self, thing):
        self.things.append(thing)
        return self.things

    def __str__(self):
        result = ""
        for i in range(0, len(self.things)):
            result += str(i+1) + ". " + self.things[i].__str__() + "\n"
        return result
