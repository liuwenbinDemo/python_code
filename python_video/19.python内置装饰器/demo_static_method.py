"""
多轮比赛，每轮由两个不同的英雄对打
"""
class Game:

    def __init__(self, first_hero, second_hero):
        self.first_hero = first_hero
        self.second_hero = second_hero
    # fight 有和实例变量交互的部分，所以需要定义为一个普通方法
    def fight(self):
        print(f"本轮比赛开始，由{self.first_hero} VS {self.second_hero}")

    # start 没有和类或实例交互的部分，那么就可以使用staticmethod
    @staticmethod
    def start():
        print("游戏开始")

Game.start()
game1 = Game("Bob", "Mary")
game2 = Game("Mike", "Henry")
game1.fight()
game2.fight()