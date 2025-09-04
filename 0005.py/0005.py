class Animal:
    def __init__(self,name,age,species):
        self.name=name
        self.age=age
        self.species=species
    def info(self):
        print(f"Name: {self.name}\nAge: {self.age} years\nSpecies: {self.species}")

class Dog(Animal):
    def __init__(self,name,age,species,breed):
        super().__init__(name,age,species)
        self.breed=breed
    def info(self):
        super().info()
        print(f"Breed: {self.breed}")

class Cat(Animal):
    def __init__(self,name,age,species,color):
        super().__init__(name,age,species)
        self.color=color
    def info(self):
        super().info()
        print(f"Color: {self.color}")

x=Dog("Milo",2,"Dog","Husky")
x.info()

y=Cat("Candy",3,"Tabby","Orange")
y.info()