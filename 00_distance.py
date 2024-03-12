#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pprint import pprint
# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']

dist_Moscow_London = ((moscow[0]-london[0])**2+(moscow[1]-london[1])**2)**0.5
dist_Moscow_Paris = ((moscow[0]-paris[0])**2+(moscow[1]-paris[1])**2)**0.5
dist_London_Paris = ((london[0]-paris[0])**2+(london[1]-paris[1])**2)**0.5

#test print(dist_Moscow_London)

MOSCOW = {}
MOSCOW['Moscow_to_London'] = dist_Moscow_London
MOSCOW['Moscow_to_Paris'] = dist_Moscow_Paris

LONDON = {}
LONDON['London_to_Moscow']= dist_Moscow_London
LONDON['London_to_Paris']= dist_London_Paris

PARIS = {}
PARIS['Paris_to_Moscow'] = dist_Moscow_Paris
PARIS['Paris_to_London'] = dist_London_Paris


# test print(MOSCOW)

distances = {
    'dist_Moscow':[MOSCOW],
    'dist_London':[LONDON],
    'dist_Paris':[PARIS]
}
pprint(distances)


