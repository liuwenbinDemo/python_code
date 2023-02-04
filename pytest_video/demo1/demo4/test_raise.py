"""
__author__ = 'hogwarts_xixi'
"""
import pytest


def test_raise():
  with pytest.raises((ZeroDivisionError,ValueError)):
    raise ZeroDivisionError("除数为0")

def test_raise1():
  with pytest.raises(ValueError) as exc_info:
    raise ValueError("value must be 42")
  assert exc_info.type is ValueError
  assert exc_info.value.args[0] == "value must be 42"