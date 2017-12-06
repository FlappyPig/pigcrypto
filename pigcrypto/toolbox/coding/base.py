# -*- coding: utf-8 -*-
from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long
import primefac
import urllib
import base64


def base16en(str):
    """
    :param str:
    :return:
    """
    return base64.b16encode(str)


def base16de(str):
    """
    :param str:
    :return:
    """
    return base64.b16decode(str)


def base32en(str):
    """
    :param str:
    :return:
    """
    return base64.b32encode(str)


def base32de(str):
    """
    :param str:
    :return:
    """
    return base64.b32decode(str)


def base64en(str):
    """
    :param str:
    :return:
    """
    return base64.b64encode(str)


def base64de(str):
    """
    :param str:
    :return:
    """
    return base64.b64decode(str)

def base36en(number, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    
    """Converts an integer to a base36 string."""
    if not isinstance(number, (int, long)):
        raise TypeError('number must be an integer')

    base36 = ''
    sign = ''

    if number < 0:
        sign = '-'
        number = -number

    if 0 <= number < len(alphabet):
        return sign + alphabet[number]

    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36

    return sign + base36


def base36de(number):
    return int(number, 36)


def genprime(nbit):
    """
    :param nbit: the lenth of the prime number which you want to generate
    :return: the n bit prime number
    """
    return getPrime(nbit)


def num2str(num):
    """
    :param num: a number
    :return: a str
    """
    return long_to_bytes(num)


def str2num(str):
    """
    :param str: a str
    :return: a num
    """
    return bytes_to_long(str)


def hex2str(hex):
    """
    :param hex: a hex str ('0xfffffff' or 'fffffff' or '0xfffffffffffL')
    :return: a str
    """
    if hex[0:2] == "0x":
        hex = hex[2:]
    if hex[-1] == "L":
        hex = hex[0:-1]
    if len(hex) % 2 == 0:
        return hex.decode("hex")
    else:
        return ("0" + hex).decode("hex")


def hex2num(hex):
    """
    :param hex: a hex str ('0xfffffff' or 'fffffff' or '0xfffffffffffL')
    :return: a num
    """
    if hex[0:2] == "0x":
        hex = hex[2:]
    if hex[-1] == "L":
        hex = hex[0:-1]
    return int(hex, 16)


def num2hex(num):
    """
    :param num: a num
    :return: a hex str ('0xfffffff' or '0xfffffffffffL')
    """
    return hex(num)


def str2hex(str):
    """
    :param str: a str
    :return: a hex str ('0xfffffff' or '0xfffffffffffL')
    """
    return str.encode("hex")


def modinv(e, phin):
    """
    :param e: you know, and i don't want to say anything
    :param phin: you know, and i don't want to say anything
    :return: you know, and i don't want to say anything
    """
    return primefac.modinv(e, phin) % phin


def gcd(a, b):
    """
    :param a:
    :param b:
    :return:
    """
    return primefac.gcd(a, b)


def gcdmul(lista):
    """
    :param lista: a list include all numbers you wang to calc the gcd
    :return: the gcd result
    """
    final = lista[0]
    for i in range(1, len(lista)):
        final = gcd(final, lista[i])
    return final


def urlencode(str):
    """
    :param str: a str
    :return:
    """
    return urllib.quote_plus(str)


def urldecode(str):
    """
    :param str:
    :return:
    """
    return urllib.unquote_plus(str)



