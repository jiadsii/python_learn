# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     01_走马灯
   Description :
   email:         17334029932@163.com
   Author :       duweixiao
   date：          2/14/21
"""
import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        #os.system('cls')
        os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()