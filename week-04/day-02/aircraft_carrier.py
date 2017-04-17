class Aircraft():
    def __init__(self, type_of_aircraft, ammo = 0, max_ammo = 0, base_damage = 0):
        self.type_of_aircraft = type_of_aircraft
        self.ammo = ammo
        self.max_ammo = max_ammo
        self.base_damage = base_damage
        pass

    def fight(self):
        damage = self.ammo * self.base_damage
        ammo = 0
        return damage
        #resets ammo to 0
        #returns damage
        #damage = base damage * ammo

    def refill(self, given_ammo):
        self.given_ammo = given_ammo
        #from the given number it takes as much ammo as it can
        #max the max ammo
        #returns ramaining ammo
        pass

    def get_type(self):
        #returns type as string
        pass

    def get_status(self):
        #returns type, ammo, base damage and all damage as string
        pass

class F16(Aircraft):
    def __init__(self):
        pass

class F35(Aircraft):
    def __init__(self):
        pass
