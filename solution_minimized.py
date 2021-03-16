# -*- coding: utf-8 -*-
import math; zadacha1, zadacha2, zadacha3, zadacha4, zadacha5 = lambda x: math.factorial(x), lambda x, y: x**y, lambda x, y: str(x).replace(str(y), ''), lambda x, y: sum(map(int, [str(i)+str(j)+str(k) for i in range(1, x+1) for j in range(1, x+1) for k in range(1,x+1) if i+j+k==y])), lambda m, n: {i: [j for j in range(2, i) if i % j == 0] for i in range(m, n+1)}

"""
print(zadacha1(int(input('Введите число, для которого надо найти факториал: '))))
print(zadacha2(int(input('Число, возводимое в степень: ')), int(input('Укажите степень: '))))
print(zadacha3(int(input('Натуральное число: ')), int(input('Число, которое нужно удалить: '))))
print(zadacha4(int(input('Предел: ')), int(input('Сумма цифр: '))))
print(zadacha5(int(input('От: ')), int(input('До: '))))
"""

# Красивый вывод для 5 задачи
"""
result = zadacha5(int(input('От: ')), int(input('До: ')))
for i in result.keys():
    print(f'Делители числа {i}: {result[i]}')
"""
