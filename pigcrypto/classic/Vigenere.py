#!/usr/bin/env python
# -*- coding: utf-8 -*-

def en_Vigenere(input,key):
    """
    :param input:
    :param key:
    :return:
    """
    ptLen = len(input)
    keyLen = len(key)
    quotient = ptLen // keyLen    #商
    remainder = ptLen % keyLen    #余
    out = ""
    for i in range(0, quotient) :
        for j in range(0, keyLen) :
            c = int((ord(input[i*keyLen+j]) - ord('a') + ord(key[j]) - ord('a')) % 26 + ord('a'))
            out += chr (c)
    for i in range(0,remainder) :
        c = int((ord(input[quotient*keyLen+i]) - ord('a') + ord(key[i]) - ord('a')) % 26 + ord('a'))
        out += chr(c)
    return out

def de_Vigenere(output,key):
    """
    :param output:
    :param key:
    :return:
    """
    ptLen = len(output)
    keyLen = len(key)
    quotient = ptLen // keyLen
    remainder = ptLen % keyLen
    inp = ""
    for i in range(0, quotient):
        for j in range(0, keyLen):
            c = int((ord(output[i*keyLen+j]) - ord('a') + 26 - (ord(key[j]) - ord('a')) % 26 + ord('a')))
            inp += chr(c)
    for i in range(0, remainder):
        c = int((ord(output[quotient*keyLen + i]) - ord('a') + 26 - (ord(key[i]) - ord('a')) % 26 + ord('a')))
        inp += chr(c)
    return inp


if __name__ == '__main__':
    main()