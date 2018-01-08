#!/usr/bin/env
#coding=utf-8


"""
曲路密码(Curve Cipher)是一种换位密码，需要事先双方约定密钥(也就是曲路路径)。

"""


def set_en_key(message,x,y):
    """
    :param message:  The string to be encrypted

    :param x: The number of lines specified in advance
    :param y: The number of columns specified in advance

    :return: key list
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

def set_de_key(Cipher,x,y):
    global e
    e = []

    for i in range(0,len(Cipher),y):

        e.append(Cipher[i:i+y])
    print(e)
    return e
def create_cipher_re(x,y,new_str):
    """
    reverse

    :return:
    """
    for i in reversed(range(y)):
        for j in reversed(range(x)):
            new_str += e[i][j]
            break
    return(str(new_str))
    print(new_str)

def create_cipher_po(x,y,new_str):
    """
    positive

    :return:
    """
    for i in range(y):
        for j in reversed(range(x)):
            new_str += e[i][j]
            break
    print(new_str)
    return (str(new_str))







def curve_cipher_en(message,x,y):
    set_en_key(message,x,y)
    new_str = ''
    out_put_str = ''

    for i in reversed(range(x+1)):
        if x%2 == 0:
            if i%2 == 0:

                out_put_str += create_cipher_re(i,y,new_str)
            else:
                out_put_str += create_cipher_po(i,y,new_str)
        else:
            if i%2 == 0:
                #print(str(i)+" 正向：")
                out_put_str += create_cipher_po(i,y,new_str)
            else:
                #print(str(i)+" 逆向：")
                out_put_str += create_cipher_re(i,y,new_str)
    print (out_put_str)
    return out_put_str


def create_message_re(x,y,new_str):

    for i in reversed(range(x)):
        for j in reversed(range(y)):
            new_str += e[i][j]
            break
        print(i,j,new_str)
        break
    return (new_str)





def create_message_po(x,y,new_str):

    for i in reversed(range(x)):
        for j in range(y):
            new_str += e[i][j]
            break
        print(i, j, new_str)
        break

    return (new_str)


def curve_cipher_de(Cipher,x,y):
    """
    :param Cipher:
    :param x: The number of lines specified in advance
    :param y: The number of columns specified in advance

    :return:

    """
    set_de_key(Cipher,x,y)
    a = []
    new_str = ''
    out_put_str = ''

    if x%2 == 0:
        for i in reversed(range(x)):
            if i %2==0:
                for k in range(len(e[i])):
                    print(e[i])
                    print(e[i][k])
            else:
                for k in range(len(e[i])):
                    print(e[i])
                    print(e[i][k])
    else:
        for i in reversed(range(x)):
            if i %2==0:
                for k in reversed(range(len(e[i]))):
                    new_str += e[i][k]
                a.append(new_str)
                new_str = ''
            else:
                for k in range(len(e[i])):

                    new_str += e[i][k]
                a.append(new_str)
                new_str = ''

    for i in range(y):
        for j in range(x):
            out_put_str += a[j][i]

    print(out_put_str)








if __name__ == '__main__':
    curve_cipher_en('The quick brown fox jumps over the lazy dog',7,5)
    curve_cipher_de('gesfcinphodtmwuqouryzejrehbxvalookT',7,5)