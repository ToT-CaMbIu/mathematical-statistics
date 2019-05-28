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


def theoretical_func(x):
    if x != 0:
        return 7 / 6 - 1 / (3 * x)
    return 0


def empirical_func(x, y):
    cur = -10e9
    ind = 0
    for i in range(len(y)):
        if cur >= x:
            break;
        cur = y[i]
        ind += 1
    return (ind - 1) / len(y)


def kolm(y):
    cur = 0.0
    for i in range(0, len(y)):
        cur = max(abs(empirical_func(y[i], y) - theoretical_func(y[i])), cur)
    print(np.sqrt(len(y)) * cur)


def mises(y):
    D = []
    for i in range(0, len(y)):
        D.append((theoretical_func(y[i]) - (i + 0.5) / len(y)) ** 2)
    C = 1 / (12 * len(y))
    for tmp in D:
        C += tmp
    print(C)


def prim(y):
    n = len(y)
    v = int(n / (int(np.log2(n)) + 1))
    r = v - 1
    A, B, V, P = [], [], [], []
    A.append(y[0])
    B.append((y[r] + y[r + 1]) / 2)
    V.append(v)
    l = r
    cur = v
    r += v
    while True:
        if n - cur <= v:
            A.append((y[l] + y[l + 1]) / 2)
            B.append(y[n - 1])
            V.append(n - cur)
            break
        A.append((y[l] + y[l + 1]) / 2)
        B.append((y[r] + y[r + 1]) / 2)
        l = r
        r += v
        V.append(v)
        cur += v

    X = 0
    P = 0
    for (a, b, v) in zip(A, B, V):
        p = theoretical_func(b) - theoretical_func(a)
        P += p
        X += ((v - n * p) ** 2) / (n * p)
    print(X)
    print(P - 1)
    print('+' if abs(P - 1) <= 0.01 else '-')


def main():
    n = 200
    x, y = make_selection(n)
    y.sort()
    print("Вариационный ряд:")
    print(y)
    prim(y)
    kolm(y)
    mises(y)


if __name__ == '__main__':
    main()
# 18.48
# 1.63
# 0.744
