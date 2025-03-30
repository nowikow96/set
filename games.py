from random import randint as r
import json

from config_bot import My_Message

mess_info = My_Message()


class Games_Guess:

    def __init__(self, id: int):
        self.id = id
        self.random_value = r(0, 100)

    def proba(self, user_value: int) -> str:
        if user_value > self.random_value:
            return mess_info.men
        elif user_value < self.random_value:
            return mess_info.bol
        else:
            return mess_info.win


game = Games_Guess(123)

for i in range(8):
    x = int(input())
    print(game.proba(x))
