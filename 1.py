class Student:
    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = grades
        self.subject = None 

    def display_info(self):
        print(f"Student: {self.name} {self.surname}")
        print("Známky:", ", ".join(map(str, self.grades)))
        if self.subject:
            print(f"Předmět: {self.subject}")

    def add_subject(self, subject): 
        self.subject = subject


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def add_grade(self, student, grade):  
        if student.subject == self.subject:
            student.grades.append(grade)
            print(f"Hodnocení {grade} bylo přidáno studentovi {student.name} {student.surname}")
        else:
            print(f"Chyba: Student {student.name} {student.surname} není zapsán na předmětu {self.subject}")


student1 = Student("Alexandr", "Dulovec", [1, 1, 1])
student1.display_info()

student1.add_subject("Webové programování")

teacher1 = Teacher("Bc. Martin Kokeš", "Webové programování")
teacher1.add_grade(student1, 2)
student1.display_info()
