# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

print('Введите с клавиатуры через пробел диапазон значений min и max и длину списка')

list_var = tuple(map(int, input('Введите значения: ').split()))

new_list = [random.randint(0, list_var[1] + 10) for _ in range(list_var[2])]

print(new_list)

for elem in new_list:
    if list_var[0] <= elem <= list_var[1]:
        print(new_list.index(elem))