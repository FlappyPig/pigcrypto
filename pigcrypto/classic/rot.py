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
    
    c = ord(letter)
    if c == 32:
        return chr(int(c))
    else:
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
        
def de_rot_ascii(cipher,n):

    new_str = ''
    for i in str(cipher):
        i = ord(i)-int(n)
        i = chr(i)
        new_str += i
    return new_str

def en_rot_ascii(cipher,n):
    
    new_str = ''
    for i in str(cipher):
        i = ord(i)+int(n)
        new_str += chr(i)

    return new_str


def test():
    print ('test')
    print (rot('flappypig is cool',13))
    print (rot('syncclcvt vf pbby',13))
    print (rot_loop('syncclcvt vf pbby'))
    print (de_rot_ascii('D5Y8h5H|]mP3PGD|RGokPmTqPZYK]JQoPmH|Q}IpPGEpQZH6iT@@',3))
    print (en_rot_ascii('A2V5e2EyZjM0MDAyODlhMjQnMWVHZGNlMjEyNzFmMDBmNWE3fQ==',3))


if __name__ == '__main__':
    test()