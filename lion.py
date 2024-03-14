import tiger
class Lion:
    def init(self, name):
        self.name = name

    def roar(self):
        print(f"{self.name} roars loudly!")

    def attack(self):
        print(f"{self.name} attacks with its sharp claws!")
        
# Create an instance of the Lion class
name = input("Enter Lion name: ")

my_lion = Lion(name)
my_lion.roar()
my_lion.attack()