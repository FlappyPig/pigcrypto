#!/usr/bin/env
#coding=utf-8


"""
曲路密码(Curve Cipher)是一种换位密码，需要事先双方约定密钥(也就是曲路路径)。

"""


def set_key(message,x,y):
    """
    :param message:  The string to be encrypted

    :param x: The number of lines specified in advance
    :param y: The number of columns specified in advance

    :return:
    """
    #message = 'The quick brown fox jumps over the lazy dog'

    global e
    e = []
    a = list(message.replace(' ',''))
    for i in range(1,y+1):
        m = x*(i-1)
        n = x*i
        b = a[m:n]
        e.append(b)
    return e






def curve_cipher_en(message,x,y):
    set_key(message,x,y)
    new_str = ''

    #set_flag = 0
    if x % 2 ==0:
        set_flag = 0
    else:
        set_flag =1


    for i in reversed(range(y)):
        for j in reversed(range(x)):
            new_str += e[i][j]
            break 
    print(new_str)







if __name__ == '__main__':
    curve_cipher_en('The quick brown fox jumps over the lazy dog',7,5)