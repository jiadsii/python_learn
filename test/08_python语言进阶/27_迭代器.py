# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     27_迭代器
   Description :
   email:         17334029932@163.com
   Author :       duweixiao
   date：          2/18/21
"""


class Fib(object):
    """迭代器"""

    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration()