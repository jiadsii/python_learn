# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     04_itertools
   Description :
   email:         17334029932@163.com
   Author :       duweixiao
   date：          2/18/21
"""
"""
迭代工具模块
"""
import itertools

# 产生ABCD的全排列
print(itertools.permutations('ABCD'))
# 产生ABCDE的五选三组合
itertools.combinations('ABCDE', 3)
# 产生ABCD和123的笛卡尔积
itertools.product('ABCD', '123')
# 产生ABC的无限循环序列
itertools.cycle(('A', 'B', 'C'))