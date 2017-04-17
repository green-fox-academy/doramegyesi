class Aircraft():
    def __init__(self, type_of_aircraft, ammo = 0, max_ammo = 0, base_damage = 0):
        self.type_of_aircraft = type_of_aircraft
        self.ammo = ammo
        self.max_ammo = max_ammo
        self.base_damage = base_damage
        pass

    def fight(self):
        damage = self.ammo * self.base_damage
        self.ammo = 0
        return damage

    def refill(self, given_ammo):
        self.given_ammo = given_ammo
        if given_ammo <= self.max_ammo:
            self.ammo += given_ammo
            given_ammo -= self.ammo
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
    #store of ammo as a number
    def __init__(self, all_the_aircrafts, initial_ammo, health_point):
        self.all_the_aircrafts = []
        self.initial_ammo = initial_ammo
        self.health_point = health_point
        pass

    def add_aircraft(self):
        if type_of_aircraft == "F16":
            self.all_the_aircrafts.append() #what the hell should I append here
        elif type_of_aircraft == "F35":
            self.all_the_aircrafts.append() #and here too
        else:
            print("no such aircraft exists")

    def fill(self):
        #fills the aircrafts and takes the ammo needed from storage
        #for F35 first if there isnt enough for all the aircrafts
        #else:
        #    print("the ammo storage is empty!")
        pass

    def fight(self):
        #no idea what it should do exactly
        pass

    def get_status(self):
        #gives a status of the carrier ans all the aircrafts like above
        #if health point is 0 then print it's dead Jim :(
        pass

aircraft_one = Aircraft("F16", 0, 8, 30)
aircraft_two = Aircraft("F35", 0, 12, 50)
print(aircraft_one.refill(100))
print(aircraft_one.get_status())
print(aircraft_one.fight())
print(aircraft_one.get_status())
