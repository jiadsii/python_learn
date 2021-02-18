# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     10_顺序查找
   Description :
   email:         17334029932@163.com
   Author :       duweixiao
   date：          2/18/21
"""
def seq_search(items, key):
    """顺序查找"""
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1