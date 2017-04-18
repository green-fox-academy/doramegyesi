class Aircraft():
    def __init__(self, type_of_aircraft, ammo = 0, max_ammo = 0, base_damage = 0):
        self.type_of_aircraft = type_of_aircraft
        self.ammo = ammo
        self.max_ammo = max_ammo
        self.base_damage = base_damage

    def fight(self):
        damage = self.ammo * self.base_damage
        self.ammo = 0
        return damage

    def refill(self, given_ammo):
        self.given_ammo = given_ammo
        if given_ammo <= self.max_ammo:
            self.ammo += given_ammo
            given_ammo -= self.ammo
            return given_ammo
        elif given_ammo > self.max_ammo:
            self.ammo = self.max_ammo
            given_ammo -= self.max_ammo
            return given_ammo

    def get_type(self):
        return self.type_of_aircraft

    def get_status(self):
        status = "type: " + str(self.type_of_aircraft) + ", ammo: " + str(self.ammo) + ", base_damage: " + str(self.base_damage) + ", all damage: " + str(self.ammo * self.base_damage)
            #prints all damage wrong, needs to be fixed!!!
        return status

class AircraftCarrier():
    def __init__(self, initial_ammo = 0):
        self.all_the_aircrafts = []
        self.initial_ammo = initial_ammo
        self.stored_ammo = 5000
        self.health_point = 800

    def add_aircraft(self, type_of_aircraft = ""):
        if type_of_aircraft == "F16":
            self.all_the_aircrafts.append("F16") #what the hell should I append here
        elif type_of_aircraft == "F35":
            self.all_the_aircrafts.append("F35") #and here too
        else:
            print("no such aircraft exists")

    def fill(self):
        if self.stored_ammo == 0:
            print("the ammo storage is empty!")
        else:
            for n in all_the_aircrafts:
                if get_type == "F35":
                #refill
                    pass
            for n in all_the_aircrafts:
                if get_type == "F16":
                #refill it dude
                    pass

    def fight(self):
        #no idea what it should do exactly
        pass

    def get_status(self):
        if self.health_point <= 0:
            print("It's dead, Jim:(")
        #gives a status of the carrier ans all the aircrafts like above
        pass

carrier = AircraftCarrier(80)
carrier.add_aircraft("F16")
carrier.add_aircraft("F35")
print(carrier.all_the_aircrafts)
aircraft_one = Aircraft("F16", 0, 8, 30)
aircraft_two = Aircraft("F35", 0, 12, 50)
print(aircraft_one.refill(100))
print(aircraft_one.get_status())
print(aircraft_one.fight())
print(aircraft_one.get_status())
