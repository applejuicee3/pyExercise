import random

acronyms = ['HAHAHA', 'HIHIHI','HUHUHU','HOHOHOHO','HEHEHEHE']
for X in acronyms:
    print(X)
    
    r1 = random.random()
    print(r1)
    
    r2 = random.choice([1,2,3,4,5])
    print(r2)
    
    r3 = random.randint(4,4000)
    print(r3)
    
total = 0
expense = []
for i in range(5):
    expense.append(float((input("Enter a number : "))))   
    total = sum(expense)
print("total", total)


loot = ""
roll = random.randint(1,3)
print(roll)
if roll == 1 :
    loot="gold"