class Animal:
    def __init__(self,name,age,species):
        self.name=name
        self.age=age
        self.species=species
    def make_sound(self):
        print ("sound Of .......")
class Lion(Animal):
    def make_sound(self):
        print (f"{self.name} : sound Of Lion roar")
    def hunt (self,mane_size):
        self.mane_size=mane_size
        print (f" mane_size :  {self.mane_size}")
class Elephant(Animal):
    def make_sound(self):
        print (f"{self.name} : sound Of Elephant trumpet")
    def swing_trunk(self,trunk_length):
        self.trunk_length=trunk_length
        print (f" trunk_length :  {self.trunk_length}")
class Monkey(Animal):
    def make_sound(self):
        print (f"{self.name} : sound Of Monkey chatter")
    def swing(self,tail_length):
        self.tail_length=tail_length
        print (f" tail_length : {self.tail_length}")
elephant=Elephant("Mimo",3,"Thailand")
elephant.make_sound()
elephant.swing_trunk(0.5)
lion=Lion("Simba",3,"Africa")
lion.make_sound()
lion.hunt(4)
monkey=Monkey("Fibo",3,"USA")
monkey.make_sound()
monkey.swing(0.5)