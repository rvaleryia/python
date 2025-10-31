class Students:
    def __init__(self, name, age, grades: list[float]):
        self.name = name
        self.age = age
        self.grades = grades

    def get_avg_grades(Students):
        return sum(Students.grades) / len(Students.grades)

Student1 = Students("Ivan", 20, [8,10,5,9])
Student2 = Students("Lera", 21, [5,9,10,9])
Student3 = Students("Petr", 20, [8,8,7,10])

print(Student1.get_avg_grades())
print(Student2.get_avg_grades())
print(Student3.get_avg_grades())






