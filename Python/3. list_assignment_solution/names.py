names = ['Monkey D Luffy', 'Roronoa Zoro', 'Catbugler Nami', 'Sniper Ussop', 'Vinsmoke Sanji', 'Tony Tony Chopper', 'Robin', 'Franky', 'Brook', 'Jimbei']
print(len(names))
print('Welcome on board', names[0])
print('Welcome on board', names[1])
print('Welcome on board', names[2])
print('Welcome on board', names[3])
print('Welcome on board', names[4])
print('Welcome on board', names[5])
print('Welcome on board', names[6])
print('Welcome on board', names[7])
print('Welcome on board', names[8])
print('Welcome on board', names[9])

# Adding
names.append('Vivi')
print(names)

# inserting
names.insert(11, 'Vegapunk')
print(names)

# modifying
names[10] = 'Boney'
print(names)

# deleteing
del names[11]
print(names)

# poping
names.pop()
print(names)

names.pop(3)
print(names)

# removing
names.remove('Jimbei')
print(names)

# temporary sorting
print(sorted(names))
print(names)

# sorting
names.sort()
print(names)

# reverse
names.reverse()
print(names)

# temporary sorting and reversing
print(sorted(names, reverse=True))
print(names)

for name in names:
    print(name)