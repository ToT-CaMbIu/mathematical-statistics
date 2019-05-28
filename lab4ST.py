#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from prettytable import PrettyTable
import numpy as np
import math as mth
import sympy as sp
import random as rnd
import matplotlib.pyplot as plt
import matplotlib
import decimal

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


def HelperM(y, d, m, flg_d, flg_m, size):
    m_t = 0
    if not flg_m:
        for i in y:
            m_t += i
        m_t /= len(y)
    else:
        m_t = m
    d_t = 0
    if not flg_d:
        for i in y:
            d_t += (i - m_t) ** 2
        d_t *= 1 / (len(y) - 1)
    else:
        d_t = d
    mas = []
    if not flg_d and size == 20:
        iter = [3.1737, 2.8609, 2.4334]
    elif not flg_d and size == 30:
        iter = [3.038, 2.7563, 2.3638]
    elif not flg_d and size == 40:
        iter = [2.975, 2.7563, 2.3312]
    else:
        iter = [2.636, 2.326, 1.960]
    print("M:")
    print(m_t)
    print("D:")
    print(d_t)
    lmt = m_t - (np.sqrt(d_t) / np.sqrt(len(y))) * iter[0]
    rmt = m_t + (np.sqrt(d_t) / np.sqrt(len(y))) * iter[0]
    mas.append((lmt, rmt, 0.99))
    lmt = m_t - (np.sqrt(d_t) / np.sqrt(len(y))) * iter[1]
    rmt = m_t + (np.sqrt(d_t) / np.sqrt(len(y))) * iter[1]
    mas.append((lmt, rmt, 0.98))
    lmt = m_t - (np.sqrt(d_t) / np.sqrt(len(y))) * iter[2]
    rmt = m_t + (np.sqrt(d_t) / np.sqrt(len(y))) * iter[2]
    mas.append((lmt, rmt, 0.95))
    return mas


def M(y, size):
    mas = HelperM(y, 0, 0, False, False, size)
    for i in range(2):
        plt.plot([(mas[i][1] - mas[i][0]), (mas[i + 1][1] - mas[i + 1][0])], [mas[i][2], mas[i + 1][2]], marker='o',
                 color='red')
    mas = HelperM(y, 0.1507, 0, True, False, size)
    for i in range(2):
        plt.plot([(mas[i][1] - mas[i][0]), (mas[i + 1][1] - mas[i + 1][0])], [mas[i][2], mas[i + 1][2]], marker='o',
                 color='black')
    plt.show()
    return mas


def D(y, m, flg_m, size):
    if flg_m:
        m_t = m
        sum = 0
        for i in y:
            sum += (i - m_t) ** 2
        if size == 20:
            iterl, iterr = [39.99685, 37.56623, 34.16961], [7.43384, 8.26040, 9.59078]
        if size == 25:
            iterl, iterr = [46.92789, 44.31410, 40.64647], [10.51965, 11.52398, 13.11972]
        if size == 30:
            iterl, iterr = [53.67196, 50.89218, 46.97924], [13.78672, 14.95346, 16.79077]
        mas = []
        lmt = sum / iterl[0]
        rmt = sum / iterr[0]
        mas.append((lmt, rmt, 0.99))
        lmt = sum / iterl[1]
        rmt = sum / iterr[1]
        mas.append((lmt, rmt, 0.98))
        lmt = sum / iterl[2]
        rmt = sum / iterr[2]
        mas.append((lmt, rmt, 0.95))
        for i in range(2):
            plt.plot([(mas[i][1] - mas[i][0]), (mas[i + 1][1] - mas[i + 1][0])], [mas[i][2], mas[i + 1][2]], marker='o',
                     color='red')
    else:
        mas = []
        if size == 20:
            iterl, iterr = [38.58226, 36.19087, 32.85233], [6.84397, 7.63273, 8.90652]
        if size == 25:
            iterl, iterr = [45.55851, 42.97982, 39.36408], [9.88623, 10.85636, 12.40115]
        if size == 30:
            iterl, iterr = [52.33562, 49.58788, 45.72229], [13.12115, 14.25645, 16.04707]
        m_t = 0
        for i in y:
            m_t += i
        m_t /= len(y)
        d_t = 0
        for i in y:
            d_t += (i - m_t) ** 2
        d_t *= 1 / (len(y) - 1)
        const = ((len(y) - 1) * d_t)
        lmt = const / iterl[0]
        rmt = const / iterr[0]
        mas.append((lmt, rmt, 0.99))
        lmt = const / iterl[1]
        rmt = const / iterr[1]
        mas.append((lmt, rmt, 0.98))
        lmt = const / iterl[2]
        rmt = const / iterr[2]
        mas.append((lmt, rmt, 0.95))
        for i in range(2):
            plt.plot([(mas[i][1] - mas[i][0]), (mas[i + 1][1] - mas[i + 1][0])], [mas[i][2], mas[i + 1][2]], marker='o',
                     color='black')
    return mas


def main():
    iter = [20, 30, 40]
    final = []
    for i in iter:
        n = i
        _, y = make_selection(n)
        y.sort()
        print("Вариационный ряд:")
        print(y)
        mas = M(y, i)
        tmp = (mas[1][1] - mas[1][0], i)
        final.append(tmp)
    for i in range(len(final) - 1):
        plt.plot([final[i][0], final[i + 1][0]], [final[i][1], final[i + 1][1]], marker='o', color='black')
    plt.show()
    iter = [20, 25, 30]
    final = []
    for i in iter:
        n = i
        _, y = make_selection(n)
        y.sort()
        print("Вариационный ряд:")
        print(y)
        mas = D(y, 0.6486, True, i)
        D(y, 0, False, i)
        tmp = (mas[1][1] - mas[1][0], i)
        final.append(tmp)
        plt.show()
    #for i in range(len(final) - 1):
        #plt.plot([final[i][0], final[i + 1][0]], [final[i][1], final[i + 1][1]], marker='o', color='black')
    #plt.show()


if __name__ == '__main__':
    main()
