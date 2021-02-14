# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     02_设计一个函数指定验证码
   Description :
   email:         17334029932@163.com
   Author :       duweixiao
   date：          2/14/21
"""
import random


def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code

if __name__ == '__main__':
    print(generate_code(5))