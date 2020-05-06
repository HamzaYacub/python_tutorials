from abc import abstractmethod

class Bird:

    fly = True
    babies = 0
    extinct = False

    def noise(self):
        print("birdnoise")

    def reproduce(self):
        self.babies += 1
    
    @abstractmethod
    def eat(self):
        pass

class Owl(Bird):

    def reproduce(self):   #polymorphism to override reproduce method
        self.babies += 6
    
    def eat(self):          #abstract method defined in child class
        print("peck, peck")

class Dodo(Bird):
    fly = False
    extinct = True

    def eat(self):
        print("nom, nom")

    def reproduce(self):
        if self.extinct == False:
            self.babies += 1
        else:
            print("Dodos are extinct, they can no longer reproduce.")

d1 = Dodo()

d1.reproduce

print(d1.babies)
