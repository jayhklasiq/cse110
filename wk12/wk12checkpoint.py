import os
os.system('cls')

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

name = []
age = []
for name_line in people:
    names = name_line.strip().split()
    name.append(names[0])
    age.append(int(names[1]))
#solving for the youngest person.
min_age = age.index(min(age))
# print (f'{age} - {name}')
print(f'The youngest person in this group is: {name[min_age]} with age {age[min_age]}')
