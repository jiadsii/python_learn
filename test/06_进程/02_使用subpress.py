# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     02_使用subpress
   Description :
   email:         17334029932@163.com
   Author :       duweixiao
   date：          2/17/21
"""
from multiprocessing import Process
from time import sleep

counter = 0


def sub_task(string):
    global counter
    while counter < 10:
        print(string, end='', flush=True)
        counter += 1
        sleep(0.01)


def main():
    Process(target=sub_task, args=('Ping',)).start()
    Process(target=sub_task, args=('Pong',)).start()


if __name__ == '__main__':
    main()