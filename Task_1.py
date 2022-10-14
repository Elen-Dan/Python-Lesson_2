import random

i = int(input('Введите диапазон:\n'))
n = list(range(i))
print(n)
# перемешаем список:
random.shuffle(n)
print('Перемешанный список:\n')
print(n)