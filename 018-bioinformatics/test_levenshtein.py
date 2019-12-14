import pytest
import numpy as np
import itertools
import Levenshtein as levenshtein_module
import python_course_levenshtein_c
import my_levenshtein

LEN = 50000
MISTAKES = 200

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


# ======= TEST YOUR FUNCTION =======

def test_same_string_has_zero_distance(string1):
    edit_distance = my_levenshtein.calculate_levenshtein(string1, string1)
    assert edit_distance == 0

def test_different_strings_have_correct_distance(string1, string2):
    edit_distance = my_levenshtein.calculate_levenshtein(string1, string2)
    assert edit_distance == levenshtein_module.distance(string1, string2)

def test_asdf_asfd_distance_is_two():
    edit_distance = my_levenshtein.calculate_levenshtein("asdf", "asfd")
    assert edit_distance == 2

def test_asf_asfd_distance_is_one():
    edit_distance = my_levenshtein.calculate_levenshtein("asf", "asfd")
    assert edit_distance == 1

def test_amazon_aazonia_distance_is_three():
    edit_distance = my_levenshtein.calculate_levenshtein("amazon", "aazonia")
    assert edit_distance == 3

# Test files don't usually have code for being directly run, but it's useless context here
if __name__ == "__main__":
    test1 = string1()
    test2 = string2(test1)
    print(test1[0:20] + '...', test2[0:20] + '...')
    print('DISTANCE: ', my_levenshtein.calculate_levenshtein(test1, test2))
