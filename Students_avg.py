class Students:
    def __init__(self, name, age, avg):
        self.name = name
        self.age = age
        self.avg = avg
students = [
    Students("Лера", 22, 5.0),
    Students("Катя", 21, 4.0),
    Students("Саша", 24, 4.1),
    Students("Петя", 20, 3.9),
    Students("Лиза", 22, 4.2)
]
for x in students:
    if x.avg > 4.1:
        print(x.name, x.age, x.avg)


