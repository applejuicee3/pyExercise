import random
# random is a library

# acronyms = ['christine','annur','nena','bobo','ruran']

# acronyms.append('christine')
# acronyms.append('annur')
# acronyms.append('nena')
# acronyms.remove('bobo')
# acronyms.append('ruran')

acronyms = ['LOL', 'IDK']
for X in acronyms:
    print(X)
    
    r1 = random.random()
    print(r1)
    
    r2 = random.choice([1,2,3,4,5])
    print(r2)
    
    r3 = random.randint([1,1000])
    print(r3)