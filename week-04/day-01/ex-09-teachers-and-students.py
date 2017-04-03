"""Create Student and Teacher classes
Student
learn()
question(teacher) -> calls the teachers answer method
Teacher
teach(student) -> calls the students learn method
answer()"""

class Student():
    def learn(self):
        print("Student is learning amazing things from teacher!")

    def question(self, teacher):
        teacher.answer()


class Teacher():
    def teach(self, student):
        student.learn()

    def answer(self):
        print("Teacher is telling smart things to student.")

berta = Student()
tibi = Teacher()

berta.question(tibi)
tibi.teach(berta)
