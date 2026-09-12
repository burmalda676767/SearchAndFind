class Student:


    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age


    def get_info(self):

            print("i am a student. my name is ", {self.name}, "and my age is", {self.age})


nick = Student(name="Nick", age="15")
nick.get_info()
kate = Student(name="Kate", age="14")
kate.get_info()




