# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     08_使用多进程对线程实行分而治之
   Description :
   email:         17334029932@163.com
   Author :       duweixiao
   date：          2/17/21
"""
from time import time


def main():
    total = 0
    number_list = [x for x in range(1, 100000001)]
    start = time()
    for number in number_list:
        total += number
    print(total)
    end = time()
    print('Execution time: %.3fs' % (end - start))


if __name__ == '__main__':
    main()