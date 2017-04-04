class Person:
    def __init__(self, name = "Jane Doe", age = 30, gender = "female"):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("Hi, I'm " + name + ", a " + age + " year old " + gender + ".")

    def get_goal(self):
        print("My goal is: Live for the moment!")

class Student(Person):
    def __init__(self, name = "Jane Doe", age = 30, gender = "female", previous_organization = "The School of Life", skipped_days = 0):
        super().__init__(name, age, gender)

    def get_goal(self):
        print("Be a junior software developer.")

    def introduce(self):
        print("Hi, I'm " + name + ", a " + age + " year old " + gender + " from " + previous_organization + " who skipped " + skipped_days + "days from the course already.")

    def skip_days(number_of_days):
        return skipped_days -= number_of_days

class Mentor(Person):
    def __init__(self, name = "Jane Doe", age = 30, gender = "female", level = "intermediate"):
        super().__init__(name, age, gender)

    def get_goal(self):
        print("Educate brilliant junior software developers.")

    def introduce(self):
        print("Hi, I'm " + name + ", a " + age + " year old " + gender + " " + level + " mentor.")

class Sponsor(Person):
    def __init__(self, name = "Jane Doe", age = 30, gender = "female", company = "Google", hired_students = "0"):
        super().__init__(name, age, gender)

    def get_goal(self):
        print("Hire brilliant junior software developers.")

    def introduce(self):
        print("Hi, I'm " + name + ", a " + age + " year old " + gender + " who represents " + company + " and hired " + hired_students + " students so far.")

    def hire(self):
        return hired_students += 1
