# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     06_简单选择排序
   Description :
   email:         17334029932@163.com
   Author :       duweixiao
   date：          2/18/21
"""
def select_sort(items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items