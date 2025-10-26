class Animals:
    """A class representing animals with basic attributes."""
    # eye = 2
    # ears = 2
    
    def __init__(self, name, eye, ears):
        self.name = name
        self.eye = eye
        self.ears = ears
        
    def eat(self):
        if self.name:
            print(self.name, "is eating")
        else:
            print("Name does not exists")
        
    def sleep(self):
        print(self.name, "is sleeping")
    
    
mammals = Animals("Baith", 2, 2)
aves = Animals("Duck", 2, 2)
pisces = Animals("Crayfish", 2, 2)
reptiles = Animals("Python", 2, 2)

reptiles.eat()

# for each_attr in reptiles:
#     print(each_attr)





"""
    Inheritance
    
    
"""

class Ave(Animals):
    def __init__(self, name, eye, ears, beak):
        super().__init__(name, eye, ears)
        self.beak = beak
        
    def fly(self):
        return f"{self.name} is flying in the sky!!!"
    

class Reptiles(Animals):
    def __init__(self, name, eye, ears):
        super().__init__(name, eye, ears)
        
    def crawl(self):
        return f"{self.name} is crawling in the bush!!!"
    

class Mammals(Animals):
    def __init__(self, name, eye, ears):
        super().__init__(name, eye, ears)
        
    def walk(self):
        return f"{self.name} is walking on the road!!!"
    

class Pisces(Animals):
    def __init__(self, name, eye, ears, body):
        super().__init__(name, eye, ears)
        self.beak = body
        
    def swim(self):
        return f"{self.name} is swimming in the river!!!"
    
    
dove = Ave("Dove", 2, 2,"beak")
Baith = Mammals("Baith", 2, 2)
tilapia = Pisces("Tilapia", 2, 2,"scale")
python = Reptiles("Python", 2, 2)

print(dove.fly())
print(Baith.walk())
print(tilapia.swim())
print(python.crawl())