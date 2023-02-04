"""
__author__ = 'hogwarts_xixi'
"""
import itertools

import pytest

numbers    = [1,2,3,4,5]
vowels     = ['a','e','i','o','u']
consonants = ['x','y','z']

cartesian = [elem for elem in itertools.product(*[numbers,vowels,consonants])]

@pytest.fixture(params=cartesian)
def someparams(request):
  return request.param

def test_something(someparams):
  pass