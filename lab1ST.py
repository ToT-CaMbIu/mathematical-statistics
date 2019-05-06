#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from prettytable import PrettyTable
import numpy as np
import math as mth
import sympy as sp
import random as rnd
import matplotlib.pyplot as plt

a = -1
b = 5


def y_func(x):
    return 2 / (x + 2)


def make_selection(n):
    x = []
    y = []
    for _ in range(n):
        tmp = rnd.random()
        x.append(tmp * (b - a) + a)
        y.append(y_func(tmp * (b - a) + a))
    return (x, y)


def make_theoretical_func():
    x_local = np.arange(2 / 7 - 0.1, 2.0 + 0.1, 0.1)
    y_local = 7 / 6 - 1 / (3 * x_local)
    plt.plot(x_local, y_local)
    plt.show()


def make_empirical_func(t, y):
    n = len(y)
    tmp = 0
    y = list(set(y))
    y.sort()
    # print(y)
    x_cur = [y[0] - abs(y[0]), y[0]]
    y_cur = [0, 0]
    tmp += t[y[0]] / n
    plt.plot(x_cur, y_cur, marker='o')
    for i in range(1, len(y)):
        x_cur = [y[i - 1], y[i]]
        y_cur = [tmp, tmp]
        tmp += t[y[i]] / n
        plt.plot(x_cur, y_cur, marker='o')
    x_cur = [y[len(y) - 1], y[len(y) - 1] * 2]
    y_cur = [1, 1]
    plt.plot(x_cur, y_cur, marker='o')
    # plt.show()


def main():
    n = int(input())
    x, y = make_selection(n)
    pt = PrettyTable()
    pt.field_names = ['x', 'y']
    for i in range(len(x)):
        pt.add_row([x[i], y[i]])
    print(pt)
    y.sort()
    t = {}
    for i in range(len(y)):
        if y[i] in t:
            t[y[i]] += 1
            continue
        t[y[i]] = 1
    print(t)
    print("Вариационный ряд:")
    print(y)
    make_empirical_func(t, y)
    make_theoretical_func()


if __name__ == '__main__':
    main()
