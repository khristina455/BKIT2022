import pytest
import sys
from unique import Unique

def test_1():
    u = Unique([1 for i in range(10)])
    assert list(u) == [1]

def test_2():
    u = Unique(['Red', 'bLue', 'pinK', 'reD', 'greeen', 'purple', 'Purple  ', 'green'], ignore_case = True)
    assert list(u) == ['Red', 'bLue', 'pinK', 'greeen', 'purple', 'green']

def test_3():
    u = Unique(['Red', 'bLue', 'pinK', 'reD', 'greeen', 'Purple', 'Purple  ', 'green'], ignore_case = False)
    assert list(u) == ['Red', 'bLue', 'pinK', 'reD', 'greeen', 'Purple', 'green']


