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


alphabet_to_morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "Ä": ".-.-",
    "Ü": "..--",
    "ß": "...--..",
    "À": ".--.-",
    "È": ".-..-",
    "É": "..-..",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    ";": "-.-.-.",
    "?": "..--..",
    "-": "-....-",
    "_": "..--.-",
    "(": "-.--.",
    ")": "-.--.-",
    "'": ".----.",
    "=": "-...-",
    "+": ".-.-.",
    "/": "-..-.",
    "@": ".--.-.",
    "Ñ": "--.--",
    " ": " ",
    "": ""
}
morse_to_alphabet = {v: k for k, v in alphabet_to_morse.iteritems()}


def _morseremoveunusablecharacters(uncorrected_string):
    return filter(lambda char: char in alphabet_to_morse, uncorrected_string.upper())


def morseencode(decoded):
    """
    :param decoded:
    :return:
    """
    morsestring = []
    decoded = _morseremoveunusablecharacters(decoded)
    decoded = decoded.upper()
    words = decoded.split(" ")
    for word in words:
        letters = list(word)
        morseword = []
        for letter in letters:
            morseletter = alphabet_to_morse[letter]
            morseword.append(morseletter)
        word = "/".join(morseword)
        morsestring.append(word)
    return " ".join(morsestring)


def morsedecode(encoded):
    """
    :param encoded:
    :return:
    """
    characterstring = []
    words = encoded.split(" ")
    for word in words:
        letters = word.split("/")
        characterword = []
        for letter in letters:
            characterletter = morse_to_alphabet[letter]
            characterword.append(characterletter)
        word = "".join(characterword)
        characterstring.append(word)
    return " ".join(characterstring)
