import random

size = int(input('Введите размерность массива: '))
lst = [random.randint(0, 30) for i in range(size)]
minim = min(lst)
delta = int(input('Введите значение delta: '))
counter = 0
for k in range(size):
    if lst[k] - delta == minim:
        counter += 1
print(counter)