#!/usr/bin/env python
# -*- coding: utf_8 -*-



def decry(e,n):
    """

    e is ciphertext
    n is the  fence column number and mast is int 

    """
    elen=len(e)
    y=''
    for k in range(n):
        elen=len(e)
        j=1
        for i in range(0,elen,n-k):
            y+=e[i]
        for i in range(0,elen,n-k):
            e=e[:i+j-1]+e[i+j:]
            j-=1
    print('subdivision',n,'hurdle:',y)


def custom(e,n):
    """
    Custom bar number
    e is ciphertext
    n is the fence column number and mast is int
    """
    decry(e,n)

def auto(e):
    """
    Automatic traverse

    e is ciphertext
    """
    elen = len(str(e))
    l = []
    for i in range(2,elen):
        if(elen%i == 0):
            l.append(i)
    for n in l:
        decry(e,n)


def test():
    custom('fyiolpslai apgcap oa',5)
    auto('fyiolpslai apgcap oa')
if __name__ == '__main__':
    test()