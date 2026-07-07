class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display_info(self):
        print(f"Student: {self.name}, Score: {self.score}")

student1 = Student("Tommy", 72)
student2 = Student("Emma", 89)

student1.display_info()
student2.display_info()
