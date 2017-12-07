#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pigcrypto.classic.reverse import *
base = "+-0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

CODE = {
        'A': '12',     'B': '13',     'C': '14',
        'D': '15',     'E': '16',     'F': '17',
        'G': '18',     'H': '19',     'I': '20',
        'J': '21',     'K': '22',     'L': '23',
        'M': '24',     'N': '25',     'O': '26',
        'P': '27',     'Q': '28',     'R': '29',
        'S': '30',     'T': '31',     'U': '32',
        'V': '33',     'W': '34',     'X': '35',
        'Y': '36',     'Z': '37',

        'a': '38',     'b': '39',     'c': '40',
        'd': '41',     'e': '42',     'f': '43',
        'g': '44',     'h': '45',     'i': '46',
        'j': '47',     'k': '48',     'l': '49',
        'm': '50',     'n': '51',     'o': '52',
        'p': '53',     'q': '54',     'r': '55',
        's': '56',     't': '57',     'u': '58',
        'v': '59',     'w': '60',     'x': '61',
        'y': '62',     'z': '63',

        '0': '2',  '1': '3',  '2': '4',
        '3': '5',  '4': '6',  '5': '7',
        '6': '8',  '7': '9',  '8': '10',
        '9': '11',

        '+':'0'  , '-':'1'
}

def reverse(message):
    '''
     reverse
     message  -> egassem
    '''


    translated = ''

    i = len(message) - 1
    while i >= 0:
        translated = translated + message[i]
        i = i-1
    return translated


def xxencode(message):
    """
    :param message:
    :return: xxencode MESSAGE
    """
    bin_num = ''

    for i in message:
        
        roll_str = reverse(bin(ord(i))[2:]).ljust(8,'0')
        bin_num += reverse(roll_str)


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

    print(new_str)
    return new_str
    
        
def xxdecdoe(cipher):
    """
    :param cipher: Encrypted string
    :return:
    """
    bin_num = ''
    for i in cipher:
        roll_str = reverse(bin(int(CODE[i],10))[2:]).ljust(6,'0')
        bin_num += reverse(roll_str)

    new_str = ''
    for i in range(0,len(bin_num),8):

        new_str += chr(int(bin_num[i:i+8],2))

    print(new_str)
    return  new_str




if __name__ == '__main__':

    xxencode('flappypig is cool')
    xxdecdoe('NalVQ5-tQ4Zb64Zn64BjPqk')