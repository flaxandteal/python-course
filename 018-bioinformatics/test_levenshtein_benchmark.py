import pytest
import numpy as np
import itertools
import Levenshtein as levenshtein_module
import python_course_levenshtein_c
import my_levenshtein

LEN = 10
MISTAKES = 5

@pytest.fixture
def string1():
    """
    This creates a random string from four characters
    """
    return ''.join(np.random.choice(['g', 'a', 't', 'c'], size=LEN))

@pytest.fixture
def string2(string1):
    """
    This creates a string with a known number of differences to an existing string
    """
    permutations = itertools.permutations(['g', 'a', 't', 'c'])
    changed = {v[0]: v[1:] for v in permutations}

    string2 = list(string1)
    for i in np.random.choice(LEN, replace=False, size=MISTAKES):
        string2[i] = np.random.choice(changed[string1[i]])

    return ''.join(string2)

def distance(string1, string2):
    """
    This calculates the distance between two strings as a reference
    """
    return levenshtein_module.distance(string1, string2)

def test_ctypes(string1, string2, benchmark):
    string1_c = bytes(string1, encoding='ascii')
    string2_c = bytes(string2, encoding='ascii')
    edit_distance = benchmark(python_course_levenshtein_c.get_levenshtein_distance, string1_c, string2_c)

    assert edit_distance == distance(string1, string2)

#def test_pure_python(string1, string2, benchmark):
#    edit_distance = benchmark(my_levenshtein.calculate_levenshtein, string1, string2)
#
#    assert edit_distance == distance(string1, string2)

def test_matrix_python(string1, string2, benchmark):
    edit_distance = benchmark(my_levenshtein.calculate_levenshtein_matrix, string1, string2)

    assert edit_distance == distance(string1, string2)

def test_python_module(string1, string2, benchmark):
    edit_distance = benchmark(levenshtein_module.distance, string1, string2)

    assert edit_distance == distance(string1, string2)


# Test files don't usually have code for being directly run, but it's useless context here
if __name__ == "__main__":
    test1 = string1()
    test2 = string2(test1)
    print(test1[0:20] + '...', test2[0:20] + '...')
    print('DISTANCE: ', distance(test1, test2))
