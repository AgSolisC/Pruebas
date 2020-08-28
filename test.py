import pytest

from Example import rango

def test_range():

    expected_result = [1, 2, 'FIZZ', 4, 'BUZZ', 'FIZZ', 7, 8, 'FIZZ', 'BUZZ', 11, 'FIZZ', 13, 14, 'FIZZBUZZ', 16, 17, 'FIZZ', 19, 'BUZZ']
    assert rango() == expected_result