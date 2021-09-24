'''
    蛋挞篮子 最多500个，满时停3s，2元/个
    糕点师  3人
    消费者  6人，3000元/人，空时停2s，直到花完为止
'''

import time

from threading import Thread

amount = 500
money = 3000

class baker(Thread):
    name = ""
    bake = 0

    def run(self) -> None:
        global amount, money
        while True:
            if 500 > amount >= 0 and money > 0:
                self.bake = self.bake + 1
                amount = amount + 1
                print("现在还剩", amount, "个蛋挞在篮子里。")
            elif amount >= 500 and money > 0:
                amount = 500
                time.sleep(3)
            elif money == 0:
                print(self.name, "此次共制作", self.bake, "个蛋挞!")
                break

class customer(Thread):
    name = ""
    buy = 0

    def run(self) -> None:
        global amount, money
        while True:
            if 500 >= amount >0 and money > 0:
                self.buy = self.buy + 1
                amount = amount - 1
                money = money - 2
                print("还有", amount, "个蛋挞，", money, "元。")
            elif amount <= 0 and money > 0:
                amount = 0
                time.sleep(2)
            elif money == 0:
                print(self.name, "买了", self.buy, "个蛋挞!")
                break


b1 = baker()
b1.name = "b1"

b2 = baker()
b2.name = "b2"

b3 = baker()
b3.name = "b3"

c1 = baker()
c1.name = "c1"

c2 = customer()
c2.name = "c2"

c3 = customer()
c3.name = "c3"

c4 = customer()
c4.name = "c4"

c5 = customer()
c5.name = "c5"

c6 = customer()
c6.name = "c6"


c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()
b1.start()
b2.start()
b3.start()