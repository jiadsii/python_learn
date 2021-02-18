# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     20_通过装饰器实现丹丽模式
   Description :
   email:         17334029932@163.com
   Author :       duweixiao
   date：          2/18/21
"""
from functools import wraps


def singleton(cls):
    """装饰类的装饰器"""
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class President:
    """总统(单例类)"""
    pass