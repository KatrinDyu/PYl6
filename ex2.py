"""Определить индексы элементов массива (списка), значения которых принадлежат 
заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)"""

mass = [int(i) for i in input('enter massiv: ').split()]
minn = int(input('min = '))
maxx = int(input('max = '))
mass_ind = list(filter(lambda x: minn <= x <= maxx, mass))
#print(mass_ind.index())
for i in range(len(mass_ind)):
    print(mass_ind.index)

## формат вывода индекса не оговорен, значит любой (: