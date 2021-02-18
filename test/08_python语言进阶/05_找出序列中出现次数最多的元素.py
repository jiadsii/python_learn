# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     05_找出序列中出现次数最多的元素
   Description :
   email:         17334029932@163.com
   Author :       duweixiao
   date：          2/18/21
"""
"""
找出序列中出现次数最多的元素
"""
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(3))