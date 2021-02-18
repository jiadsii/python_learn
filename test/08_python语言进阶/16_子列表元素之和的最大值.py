# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     16_子列表元素之和的最大值
   Description :
   email:         17334029932@163.com
   Author :       duweixiao
   date：          2/18/21
"""
def main():
    items = list(map(int, input().split()))
    overall = partial = items[0]
    for i in range(1, len(items)):
        partial = max(items[i], partial + items[i])
        overall = max(partial, overall)
    print(overall)


if __name__ == '__main__':
    main()