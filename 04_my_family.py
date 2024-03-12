#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []
my_family = ['Mama', 'Papa']
my_family.append('Brat')
print(my_family)

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Marina',163],
    ['Andrey', 171],
    ['Stas', 183]
]
print(my_family_height)
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост отца -', my_family_height[1][1], 'cm')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
symm = my_family_height[0][1]+my_family_height[1][1]+my_family_height[2][1]
print('Общий рост моей семьи -', symm, 'cm')