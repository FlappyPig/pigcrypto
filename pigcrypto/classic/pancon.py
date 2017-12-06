#!/usr/Bin/env python
# -*- coding: utf-8 -*-
import string


ENCODE = {
	'AAAAA' : 'A' ,
	'AAAAB' : 'B' ,
	'AAABA' : 'C' ,
	'AAABB' : 'D' ,
	'AABAA' : 'E' ,
	'AABAB' : 'F' ,
	'AABBA' : 'G' ,
	'AABBB' : 'H' ,
	'ABAAA' : 'I' ,
	'ABAAB' : 'J' ,
	'ABABA' : 'K' ,
	'ABABB' : 'L' ,
	'ABBAA' : 'M' ,
	'ABBAB' : 'N' ,
	'ABBBA' : 'O' ,
	'ABBBB' : 'P' ,
	'BAAAA' : 'Q' ,
	'BAAAB' : 'R' ,
	'BAABA' : 'S' ,
	'BAABB' : 'T' ,
	'BABAA' : 'U' ,
	'BABAB' : 'V' ,
	'BABBA' : 'W' ,
	'BABBB' : 'X' ,
	'BBAAA' : 'Y' ,
	'BBAAB' : 'Z' 
	}
CODE = dict(map(lambda t:(t[1],t[0]),ENCODE.items()))

def peig(m):
    m = m.upper()
    output = ''
    for i in range(0, len(m) - 4, 5):
	    temp = m[i: i + 5]
	    output += CODE[temp]
    return output

if __name__ == '__main__':
    peig('aaaaa')