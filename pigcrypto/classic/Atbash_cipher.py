#!/usr/bin/env
#coding=utf-8

import string

"""
埃特巴什码(Atbash Cipher)是一种以字母倒序排列作为特殊密钥的替换加密，也就是下面的对应关系：

ABCDEFGHIJKLMNOPQRSTUVWXYZ
ZYXWVUTSRQPONMLKJIHGFEDCBA

明文： the quick brown fox jumps over the lazy dog

密文： gsv jfrxp yildm ulc qfnkh levi gsv ozab wlt
"""

CODE = {
	'Z' : 'A' ,
	'Y' : 'B' ,
	'X' : 'C' ,
	'W' : 'D' ,
	'V' : 'E' ,
	'U' : 'F' ,
	'T' : 'G' ,
	'S' : 'H' ,
	'R' : 'I' ,
	'Q' : 'J' ,
	'P' : 'K' ,
	'O' : 'L' ,
	'N' : 'M' ,
	'M' : 'N' ,
	'L' : 'O' ,
	'K' : 'P' ,
	'J' : 'Q' ,
	'I' : 'R' ,
	'H' : 'S' ,
	'G' : 'T' ,
	'F' : 'U' ,
	'E' : 'V' ,
	'D' : 'W' ,
	'C' : 'X' ,
	'B' : 'Y' ,
	'A' : 'Z'
	}

ENCODE = dict(map(lambda t:(t[1],t[0]),CODE.items()))

def Atbash_cipher_en(messgae):
    """

    :param messgae: The string to be encrypted
    :return: Encrypted string

    """
    new_str = ''
    upper_string = messgae.upper()
    for i in upper_string:
        if i == ' ':
            new_str += ' '
        else:
            new_str += ENCODE[i]
    print(new_str)
    return  new_str

def Atbash_cipher_de(cipher):
    """
    :param cipher: Encrypted string
    :return: clear strings
    """
    new_str = ''
    upper_string = cipher.upper()
    for i in upper_string:
        if i == ' ':
            new_str += ' '
        else:
            new_str += CODE[i]
    print(new_str)
    return  new_str



if __name__ == '__main__':
    
    Atbash_cipher_en('the quick brown fox jumps over the lazy dog')
    Atbash_cipher_de('GSV JFRXP YILDM ULC QFNKH LEVI GSV OZAB WLT')

