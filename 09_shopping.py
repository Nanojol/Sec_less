#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продукты следующего вида (писать прямо в коде)
sweets = {
    'печенье': [
        {'shop': 'ашан', 'price': 10.99},
        {'shop': 'пятерочка', 'price': 9.99},
        {'shop': 'магнит', 'price': 11.99}
    ],
    'конфеты': [
        {'shop': 'ашан', 'price': 34.99},
        {'shop': 'пятерочка', 'price': 32.99},
        {'shop': 'магнит', 'price': 30.99}
        ],
    'карамель': [
        {'shop': 'ашан', 'price': 45.99},
        {'shop': 'пятерочка', 'price': 46.99},
        {'shop': 'магнит', 'price': 41.99}
    ],
    'пирожное': [
        {'shop': 'ашан', 'price': 67.99},
        {'shop': 'пятерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99}
    ]
}
# Указать надо только по 2 магазина с минимальными ценами


pechenki_a = sweets['печенье'][0]['price']
pechenki_f = sweets['печенье'][1]['price']
pechenki_m = sweets['печенье'][2]['price']
min_pechenki = [pechenki_a,pechenki_f,pechenki_m]

candy_a = sweets['конфеты'][0]['price']
candy_f = sweets['конфеты'][1]['price']
candy_m = sweets['конфеты'][2]['price']
min_candy = [candy_a,candy_f,candy_m]

caram_a = sweets['карамель'][0]['price']
caram_f = sweets['карамель'][1]['price']
caram_m = sweets['карамель'][2]['price']
min_caram = [caram_a,caram_f,caram_m]

cake_a = sweets['пирожное'][0]['price']
cake_f = sweets['пирожное'][1]['price']
cake_m = sweets['пирожное'][2]['price']
min_cake = [cake_a,cake_f,cake_m]

def second_smallest(numbers):
    n1 = n2 = float('inf')
    for x in numbers:
        if x <= n1:
            n1, n2 = x, n1
        elif x < n2:
            n2 = x
    return n2
# # print('печенье', 'min', min(min_pechenki), 'sec_min', second_smallest(min_pechenki))
# # print('конфеты', 'min', min(min_candy), 'sec_min', second_smallest(min_candy))
# # print('карамель', 'min', min(min_caram), 'sec_min', second_smallest(min_caram))
# # print('пирожное', 'min', min(min_cake), 'sec_min', second_smallest(min_cake))
#--------------------------------------------------------------------------------------------
list_price = [
[min(min_pechenki),second_smallest(min_pechenki)],
[min(min_candy),second_smallest(min_candy)],
[min(min_caram),second_smallest(min_caram)],
[min(min_cake),second_smallest(min_cake)]
]
list_name = [
'печенье',
'конфеты',
'карамель',
'пирожное'
]
print(list_name)
for i,i_2 in list_price:
        print('min',i,'sec_min', i_2)

