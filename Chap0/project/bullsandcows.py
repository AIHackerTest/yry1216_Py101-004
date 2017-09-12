# -*- coding: utf-8 -*-
from random import *
a = randint(0, 20)
print(a) # 测试时使用，打出答案看输入正确数字是否可以正确走完流程
print("让我们来玩个游戏吧，从0到20的整数里随机挑一个数，你来猜，看对不对，只有十次机会哦。")
print("让我们开始吧。")

for i in range(1, 11):
    b = input("请输入0到20内的任意整数 > ")
    while not b.isnumeric():
        print("输入的不是整数，请重新输入。")
        b = input("请输入0到20内的任意整数 > ")
    if int(b) > a:
        print("猜的数字大了，你还有%d次机会。" % (10 - i))
        i = i + 1
        continue
    elif int(b) < a:
        print("猜的数字小了，你还有%d次机会。" % (10 - i))
        i = i + 1
        continue
    else:
        print("恭喜你！答对啦！")
        break
print("游戏结束！")
