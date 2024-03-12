#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()
Pi = 3.1415926
S = Pi*radius**2
print('Задание 1 =',round(S,4))

# Далее, пусть есть координаты точки
point = (23, 34)
# где 23 - координата х, 34 - координата у
dot_x = point[0]
dot_y = point[1]
# Если точка point лежит внутри того самого круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False
circle_mid = (0, 0)
Rad_dot = (dot_x**2+dot_y**2)**0.5
print('Раудиус точки =', round(Rad_dot, 0))
print('Задание 2', Rad_dot<=radius)

# Аналогично для другой точки
point_2 = (30, 30)
dot_x2 = point_2[0]
dot_y2 = point_2[1]
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
Rad_dot2 = (dot_x2**2+dot_y2**2)**0.5
print('Раудиус точки 2 =', round(Rad_dot2, 0))
print('Задание 3', Rad_dot2<=radius)
# Пример вывода на консоль:
#
# 77777.7777
# False
# False

