# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     29_生成器进化成进程
   Description :
   email:         17334029932@163.com
   Author :       duweixiao
   date：          2/18/21
"""
def calc_avg():
    """流式计算平均值"""
    total, counter = 0, 0
    avg_value = None
    while True:
        value = yield avg_value
        total, counter = total + value, counter + 1
        avg_value = total / counter


gen = calc_avg()
next(gen)
print(gen.send(10))
print(gen.send(20))
print(gen.send(30))