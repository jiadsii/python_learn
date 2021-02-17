# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     04_拆分长字符串
   Description :
   email:         17334029932@163.com
   Author :       duweixiao
   date：          2/17/21
"""
import re


def main():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。, .]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)  # ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡']


if __name__ == '__main__':
    main()