# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     19_通过定义类的方式定义参数器
   Description :
   email:         17334029932@163.com
   Author :       duweixiao
   date：          2/18/21
"""
from functools import wraps
from time import time


class Record():
    """通过定义类的方式定义装饰器"""

    def __init__(self, output):
        self.output = output

    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            self.output(func.__name__, time() - start)
            return result

        return wrapper