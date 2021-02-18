# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     25_用元类实现单例模式
   Description :
   email:         17334029932@163.com
   Author :       duweixiao
   date：          2/18/21
"""
import threading


class SingletonMeta(type):
    """自定义元类"""

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        cls.__lock = threading.RLock()
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class President(metaclass=SingletonMeta):
    """总统(单例类)"""

    pass