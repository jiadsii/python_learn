# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     28_生成器
   Description :
   email:         17334029932@163.com
   Author :       duweixiao
   date：          2/18/21
"""
def fib(num):
    """生成器"""
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a