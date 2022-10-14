'''
1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
 6782 -> 23
 0,56 -> 11
'''

from ast import Break


x = str(input('Введите вещественное число: '))
sum = 0
if int(x) < 0:
    print('Число меньше нуля')
    Break
else:    
    for i in range(len(x)):
        if x[i] != '.' and x[i] != ',':
            sum += int(x[i])
    print(sum)