import random
size = int(input('Введите размерность массива: '))
arr = []
for i in range(size):
    arr.append(float(input('Введите элементы массива: ')))
print('Исходный массив: \n'', arr)
index = arr.index(max(arr))
for j in range(index + 1, size):
    arr[j] = 0
print('Изменённый массив: \n'', arr)