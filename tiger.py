
class Tiger:
    def init(self, name):
        self.name = name

    def roar(self):
        print(f"{self.name} roars ferociously!")

    def attack(self):
        print(f"{self.name} pounces on its prey!")
        
# Create an instance of the Lion class
name = input("Enter Tiger name: ")

my_tiger = Tiger(name)
my_tiger.roar()
my_tiger.attack()


