# -*- coding: utf-8 -*-

import string

def rotate_letter(letter,n):
    '''
    Rotates a letter by n places.  Does not change other chars.

    letter: single  letter string
    n: int
    '''

    if letter.isupper():
        start = ord('A')
    elif letter.islower:
        start = ord('a')
    else:
        return letterpyt

    c = ord(letter)-start
    i = (c+n)%26+start
    return chr(i)


def rot(word,n):
    '''
    Rotates a word by n places.

    words : stirng

    n: integer
    '''
    res = ''
    for letter in word:
        res += rotate_letter(letter,int(n))
    return res

def rot_loop(word):
    '''
    loop 0-26 
    words :string

    '''
           
    for i in range(26):
        res = ''
        for letter in word:
            res += rotate_letter(letter,int(i))
        print('{0}: {1}'.format(i,res))
        


def test():
    print (rot('flapp ypig',13))
    print (rot('synccalcvt',13))
    print (rot_loop('synccalcvt'))


if __name__ == '__main__':
    test()