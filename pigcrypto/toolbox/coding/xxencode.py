#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pigcrypto.classic.reverse import *
base = "+-0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

#
# def reverse(message):
#     '''
#      reverse
#      message  -> egassem
#     '''
#
#
#     translated = ''
#
#     i = len(message) - 1
#     while i >= 0:
#         translated = translated + message[i]
#         i = i-1
#     return translated


def xxencode(message):
    """
    :param message:
    :return: xxencode MESSAGE
    """
    bin_num = ''

    for i in message:
        
        roll_str = reverse(bin(ord(i))[2:]).ljust(8,'0')
        bin_num += reverse(roll_str)
        #print (bin_num)
    if (len(bin_num) % 6) == 0:
        pass
        #return bin_num
    else:
        flag = len(bin_num)%6
        bin_num = bin_num.ljust(6-flag+len(bin_num),'0')  # 填充到6的倍数
        #print (bin_num)
        #return bin_num
    new_str = ''
    for i in range(0,len(bin_num),6):
        # print (bin_num[i:i+6])
        # print (int(bin_num[i:i+6],2))
        new_str += base[(int(bin_num[i:i+6],2))]
    
    return new_str
    
        




if __name__ == '__main__':

    xxencode('1phan')