# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     21_线程安全的单利模式
   Description :
   email:         17334029932@163.com
   Author :       duweixiao
   date：          2/18/21
"""
from functools import wraps
from threading import RLock


def singleton(cls):
    """线程安全的单例装饰器"""
    instances = {}
    locker = RLock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with locker:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper