'''
4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции хранятся в файле
file.txt в одной строке одно число.
'''
import random

num = int(input('Введите число: '))
numbers = []
for i in range(num):
    numbers.append(random.randint(-num, num + 1))
    
print(numbers)
print(numbers[1] * numbers[3])

result = 1
f = open('file.txt', 'r')
for line in f:
    if line == "":
        break
    result *= numbers[int(line)]
f.close()
print(result)