import random
size_a = int(input('Введите размер массива A: '))
a = [random.randint(0, 30) for i in range(size_a)]
print('Массив A: \n', a)
size_b = int(input('Введите размер массива B: '))
b = [random.randint(0, 30) for i in range(size_b)]
print('Массив B: \n', b)
com = []
for j in set(a):
    if j in b:
        com.append(j)
print('Общие элементы A и B: \n', com)