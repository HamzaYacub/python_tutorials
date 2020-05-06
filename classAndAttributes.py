class student:

    def __init__(self, name, age, __class):
        self.name = name
        self.age = age
        self.__class = __class

    def avgTestScore(self, test1, test2, test3):
        avg = round((test1 + test2 + test3) / 3)
        return avg
    
Hamza = student("Hamza", 22, "April DevOps cohort")

print(Hamza.name)
print(Hamza.age)
print(Hamza._student__class)

avgTest = Hamza.avgTestScore(12, 23, 44)
print(avgTest)
