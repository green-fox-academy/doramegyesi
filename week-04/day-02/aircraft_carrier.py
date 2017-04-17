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

    def refill(self, given_ammo):
        self.given_ammo = given_ammo
        if given_ammo <= self.max_ammo:
            self.ammo += given_ammo
            given_ammo -= self.ammo
        elif given_ammo > self.max_ammo:
            self.ammo == self.max_ammo
            given_ammo -= self.max_ammo
            return given_ammo

    def get_type(self):
        return self.type_of_aircraft

    def get_status(self):
        damage = self.fight()
        status = "type:", str(self.type_of_aircraft), "ammo:", str(self.ammo), "base_damage:", str(self.base_damage), "all damage:", str(damage)
        return status

#class F16(Aircraft):
#    def __init__(self, type_of_aircraft, ammo = 0, max_ammo = 8, base_damage =30):
#        pass

#class F35(Aircraft):
#    def __init__(self, type_of_aircraft, ammo = 0, max_ammo = 12, base_damage = 50):
#        pass

aircraft_one = Aircraft("F16", 0, 8, 30)
aircraft_two = Aircraft("F35", 0, 12, 50)
print(aircraft_one.refill(100))
print(aircraft_one.get_status())
