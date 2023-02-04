"""
__author__ = 'hogwarts_xixi'
"""
class Father:
    def father_method(self,a,b):
        print("father")
        return a+b

class TestChild(Father):
    def setup_class(self):
        print("setupclass")

    def teardown(self):
        print(Father().father_method(1,3))



    def test_aaa(self):
        print("aaa")
