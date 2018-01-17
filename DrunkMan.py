# -*- coding: utf-8 -*-
"python模拟醉汉问题"
import random as r
import matplotlib.pyplot as plt
import numpy as np


class Person:
    "醉汉类"

    def __init__(self, step=1):
        self.coor_x = 0
        self.coor_y = 0
        self.dis = 0
        self.step = step

    def move(self):
        "随机移动"
        randnum1 = r.randint(0, 1)
        randnum2 = r.randint(0, 1)
        if randnum1:
            if randnum2:
                self.coor_x += 1 * self.step
            else:
                self.coor_x -= 1 * self.step
        else:
            if randnum2:
                self.coor_y += 1 * self.step
            else:
                self.coor_y -= 1 * self.step
        self.dis = self.get_dis()

    def get_dis(self):
        "计算距离"
        return self.coor_x * self.coor_x + self.coor_y * self.coor_y


def package(times: int)->list:
    "得到一组试验结果"
    per = Person()
    res = []
    for _ in range(times):
        per.move()
        res.append(dict(x=per.coor_x, y=per.coor_y, dis=per.dis))
    return res


"""test code"""


def plot1():
    COUNT = 1000
    PLOT_TIMES = 60
    plt.xlabel("Steps")
    plt.ylabel("Distance")
    plt.title("Drunk man Random walk")
    for _ in range(PLOT_TIMES):
        "多次描图"
        DIS = np.array([x['dis'] for x in package(COUNT)])
        plt.plot(range(COUNT), DIS, label=str(_ + 1))

    plt.legend(loc='upper left')
    plt.show()


COUNT = 700
PLOT_TIMES = 10000
THRESHOLD = 1000
plt.xlabel("Distance")
plt.ylabel("Count")
plt.title("Drunk man Random walk")

RESULT = np.array(list(filter(lambda x: x < THRESHOLD,
                              [package(COUNT)[-1]['dis'] for _ in range(PLOT_TIMES)])))
plt.hist(RESULT, 200)

plt.legend(loc='upper left')
plt.show()
