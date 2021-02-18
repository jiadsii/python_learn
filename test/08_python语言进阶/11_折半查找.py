# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     11_折半查找
   Description :
   email:         17334029932@163.com
   Author :       duweixiao
   date：          2/18/21
"""
def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1