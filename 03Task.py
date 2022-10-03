# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math
my_list = [1.1, 1.2, 3.1, 5, 10.01]
new_list = []
for i in range(len(my_list)):
    elem, _ = math.modf(my_list[i])
    elem = round(elem, 4)
    new_list.append(elem)

print(new_list)
my_max = new_list[0]
my_min = new_list[0]
for i in range(len(new_list)):
    if new_list[i] > my_max and new_list[i] != 0:
        my_max = new_list[i]
    if new_list[i] < my_min and new_list[i] != 0:
        my_min = new_list[i]
res = my_max - my_min
print(my_max)
print(my_min)
print(res)
