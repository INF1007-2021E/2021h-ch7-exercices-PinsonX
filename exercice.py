#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
from turtle import *


# TODO: Définissez vos fonction ici
def mesure_ellipsoide(a, b, c, m_vol):
    vol = 4/3 * math.pi * a * b * c
    return (vol, m_vol * vol)

x = lambda dic: sorted(dic.items(), key= lambda x: x[1])[-1][0]

def draw_branch(branch_len, pen_size, angle):
    if branch_len > 0 and pen_size > 0:
        pensize(pen_size)
        forward(branch_len)
        right(angle)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        left(angle * 2)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        right(angle)
        backward(branch_len)


def draw_tree():
    setheading(90)
    color("green")
    draw_branch(70, 7, 35)
    done()


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    V, M_V = mesure_ellipsoide(1, 2, 3, 8)
    print(V, M_V)
    dic = {'s': 12, 'd':6, 'w':1, 'y':3}
    print(x(dic))
    draw_tree()