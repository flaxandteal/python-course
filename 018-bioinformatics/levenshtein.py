"""
F+T Python Course: levenshtein module

Credit where credit's due - for help with the algorithms, thanks to Wikipedia editors!
https://en.wikipedia.org/wiki/Levenshtein_distance
"""

import numpy as np

# Simple but slow method (recursive)
def calculate_levenshtein(a, b):
    if a == '':
        return len(b)
    elif b == '':
        return len(a)

    if a[-1] == b[-1]:
        cost = 0
    else:
        cost = 1

    return min(
        calculate_levenshtein(a[:-1], b) + 1,
        calculate_levenshtein(a, b[:-1]) + 1,
        calculate_levenshtein(a[:-1], b[:-1]) + cost
    )

# Iterative approach
def calculate_levenshtein_matrix(a, b):
    k = len(a) + 1
    l = len(b) + 1
    matrix = np.zeros((k, l), dtype=int)

    for i in range(1, k):
        matrix[i, 0] = i

    for j in range(1, l):
        matrix[0, j] = j

    for i in range(1, k):
        for j in range(1, l):
            if a[i - 1] == b[j - 1]:
                cost = 0
            else:
                cost = 1

            matrix[i, j] = min(
                matrix[i - 1, j] + 1,
                matrix[i, j - 1] + 1,
                matrix[i - 1, j - 1] + cost
            )

    return matrix[-1, -1]
