#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
def urlencode(str):
    """
    url编码
    """
    d = {'urlcodestr':str}
    return urllib.urlencode(d)
CODE = {
        'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',

        ',': '--..--', '.': '.-.-.-', ':': '---...', ';': '-.-.-.',
        '?': '..--..', '=': '-...-',  "'": '.----.', '/': '-..-.',
        '!': '-.-.--', '-': '-....-', '_': '..--.-', '(': '-.--.',
        ')': '-.--.-', '$': '...-..-','&': '. . . .','@': '.--.-.'
}
# 反转字典(作为解密摩斯密码的字典)
UNCODE = dict(map(lambda t:(t[1],t[0]),CODE.items()))

def s2morse(msg):
    """
    将字符串转换为摩斯密码
    :param msg: 要转换为morse密码的string
    :message: 用于保存加密结果
    :return: morse密文
    """
    message = ''
    print ("morse加密结果为:"),
    for c in msg:
        if c == ' ':
            message += ' '
        else:
            message += CODE[c.upper()] + ' '
    return message

def morse2s(morseCode):
    """
    将摩斯密码还原成字符串
    :param morseCode: morse密文
    :message: 用于保存解密结果
    :return: 明文字符串
    """
    #
    message = ''
    list = morseCode.split(' ')
    print ("morse解密结果为:"),
    for s in list:
        if s == '':
            message += ' '
        else:
            message += UNCODE[s]
    return message

if __name__ == '__main__':
    print(s2morse('flagppypig is cool'))