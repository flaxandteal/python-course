"""
F+T Python Course: levenshtein module

Credit where credit's due - for help with the algorithms, thanks to Wikipedia editors!
https://en.wikipedia.org/wiki/Levenshtein_distance
"""

import numpy as np
import python_course_levenshtein_py

# Simple but slow method (recursive)
def calculate_levenshtein(a, b):
    result = 0

    ...

    return result

# Iterative approach
def calculate_levenshtein_matrix(a, b):
    k = len(a) + 1
    l = len(b) + 1
    matrix = np.zeros((k, l), dtype=int)

    ...

    result = matrix[-1, -1]

    #Remove this
    result = python_course_levenshtein_py.calculate_levenshtein_matrix(a, b)
    #From here

    return result
