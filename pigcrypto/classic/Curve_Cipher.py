#!/usr/bin/env
#coding=utf-8


"""
曲路密码(Curve Cipher)是一种换位密码，需要事先双方约定密钥(也就是曲路路径)。

"""


def curve_cipher_de(message,x,y):
    """
    :param message:  The string to be encrypted

    :param x: The number of lines specified in advance
    :param y: The number of columns specified in advance

    :return:
    """
    message = 'The quick brown fox jumps over the lazy dog'

    set_key 