
class Cat:
    
    def __init__(self, name, breed="Pars", age=1, color="White"):
        print("Hello ", name, breed, age, color)
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        return

    

Mona = Cat("Mona", "Siem", 1, "Broun")
Tom = Cat("Tom")
# print(Mona.name)
# print(Mona)
# print(Tom)

