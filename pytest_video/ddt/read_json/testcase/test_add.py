import json

import pytest
from read_json.func.operation import my_add


def get_json():
    """
    [[1, 1, 2], [3, 6, 9], [100, 200, 300]]
    :return:
    """
    with open("../data/params.json", 'r') as file:
        data = json.loads(file.read())
        return list(data.values())

class TestWithJson:

    @pytest.mark.parametrize('x,y,expected', get_json())
    def test_add(self, x, y, expected):
        value = my_add(int(x), int(y))
        assert value == int(expected)