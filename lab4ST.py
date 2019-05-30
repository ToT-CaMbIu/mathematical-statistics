#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from prettytable import PrettyTable
import numpy as np
import math as mth
import sympy as sp
import random as rnd
import matplotlib.pyplot as plt
from scipy import stats as sc
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
    alphas = [0.99, 0.98, 0.95, 0.9]
    if not flg_d:
        for a in alphas:
            t = sc.t.isf((1 - a) / 2, len(y) - 1)
            l = m_t - (np.sqrt(d_t) / np.sqrt(len(y))) * t
            r = m_t + (np.sqrt(d_t) / np.sqrt(len(y))) * t
            mas.append((l, r, a))
    else:
        for a in alphas:
            t = sc.norm.isf((1 - a) / 2)
            l = m_t - (np.sqrt(d_t) / np.sqrt(len(y))) * t
            r = m_t + (np.sqrt(d_t) / np.sqrt(len(y))) * t
            mas.append((l, r, a))
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
        alphas = [0.99, 0.98, 0.95, 0.9]
        mas = []
        for a in alphas:
            l = sum / sc.chi2.isf((1 - a) / 2, len(y))
            r = sum / sc.chi2.isf((1 + a) / 2, len(y))
            mas.append((l, r, a))
        for i in range(len(mas) - 1):
            plt.plot([abs(mas[i][1] - mas[i][0]), abs(mas[i + 1][1] - mas[i + 1][0])], [mas[i][2], mas[i + 1][2]],
                     marker='o',
                     color='red')
    else:
        m_t = 0
        for i in y:
            m_t += i
        m_t /= len(y)
        d_t = 0
        for i in y:
            d_t += (i - m_t) ** 2
        d_t *= 1 / (len(y) - 1)
        const = ((len(y) - 1) * d_t)
        alphas = [0.99, 0.98, 0.95, 0.9]
        mas = []
        for a in alphas:
            l = const / sc.chi2.isf((1 - a) / 2, len(y) - 1)
            r = const / sc.chi2.isf((1 + a) / 2, len(y) - 1)
            mas.append((l, r, a))
        for i in range(len(mas) - 1):
            plt.plot([abs(mas[i][1] - mas[i][0]), abs(mas[i + 1][1] - mas[i + 1][0])], [mas[i][2], mas[i + 1][2]],
                     marker='o',
                     color='black')
    return mas


def main():
    iter = [30, 50, 70, 100, 150]
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
    iter = [30, 50, 70, 100, 150]
    final = []
    for i in iter:
        n = i
        _, y = make_selection(n)
        y.sort()
        print("Вариационный ряд:")
        print(y)
        mas = D(y, 0.6486, True, i)
        D(y, 0, False, i)
        tmp = (abs(mas[1][1] - mas[1][0]), i)
        final.append(tmp)
        plt.show()
    for i in range(len(final) - 1):
        plt.plot([final[i][0], final[i + 1][0]], [final[i][1], final[i + 1][1]], marker='o', color='black')
    plt.show()


if __name__ == '__main__':
    main()
