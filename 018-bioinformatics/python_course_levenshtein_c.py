from ctypes import cdll
import numpy
import timeit
import string

levenshtein_c = cdll.LoadLibrary('./levenshtein.so')

def get_levenshtein_distance(string1, string2):
    return levenshtein_c.levenshtein(string1, string2)
