import math
import matplotlib.pyplot as plt


def find_k1k2(T):
    A1 = 2*10**11
    A2 = 8*10**12
    E1 = 251000
    E2 = 297000
    R = 8.31
    k1 = A1 * math.exp(-E1/(R * T))
    k2 = A2 * math.exp(-E2 / (R * T))
    return k1, k2


def find_new_C1(m, k1, C1, dl):
    D = 0.1
    