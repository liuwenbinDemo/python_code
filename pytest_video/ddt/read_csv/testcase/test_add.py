import csv

import pytest
from read_csv.func.operation import my_add

def get_csv():
    """
    读取CSV文件
    :return: 格式：[[1, 1, 2], [3, 6, 9]]
    """

    with open('../data/params.csv') as file:
        raw = csv.reader(file)

        data = []
        for line in raw:
            data.append(line)
        print(data)
    return data

class TestWithCSV:
    @pytest.mark.parametrize('x,y,expected', get_csv())
    def test_add(self, x, y, expected):
        assert my_add(int(x), int(y)) == int(expected)