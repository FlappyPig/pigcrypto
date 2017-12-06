#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
"""
#!shell
  1  2  3  4  5
1 A  B C/K D  E
2 F  G  H  I  J 
3 L  M  N  O  P
4 Q  R  S  T  U
5 V  W  X  Y  Z

The corresponding positions of C and K are 13

"""

CODE = {
        'A': '11',     'B': '12',     'C': '13',
        'D': '14',     'E': '15',     'F': '21',
        'G': '22',     'H': '23',     'I': '24',
        'J': '25',     'K': '  ',    'L': '31',
        'M': '32',     'N': '33',     'O': '34',
        'P': '35',     'Q': '41',     'R': '42',
        'S': '43',     'T': '44',     'U': '45',
        'V': '51',     'W': '52',     'X': '53',
        'Y': '54',     'Z': '55',

}
# 反转字典(作为敲击密码的字典)
UNCODE = dict(map(lambda t:(t[1],t[0]),CODE.items()))

def tap_en(message):

    new_str = ''
    for i in message:
        if i == ' ':
            new_str += ' '
        else:
            new_str += CODE[i.upper()] + ' '
    return new_str

def tap_de(cipher):

    new_str = ''
    list = cipher.split(' ')
    for s in list:
        if s == '':
            new_str += ' '
        else:
            new_str += UNCODE[s]
    return new_str        

    



if __name__ == '__main__':
    print(tap_en('flappypig is cool'))
    print(tap_de('21 31 11 35 35 54 35 24 22  24 43  13 34 34 31'))