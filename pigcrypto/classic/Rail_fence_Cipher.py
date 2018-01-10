#!/usr/Bin/env python
# -*- coding: utf-8 -*-


def rail_fence_encode(message,inter):
    """
    inter: 
    message : 
    return : encryp
    """
    elist = []
    new_str = ''
    message = message.replace(' ','')
    for i in range(0,len(message),inter):
        
        elist.append(message[i:i+inter:])
        # print(elist)

    for i in range(inter):
        for j in range(int(len(message)/inter)+1):
            try:
                new_str += elist[j][i]
            except Exception as e:
                # print(e)
                pass

        # print(j,i,new_str)

    print(new_str)
    return new_str

def rail_fence_decode(cipher,inter):
    elist = []
    new_str = ''

    if inter == 2:

        for count in range(0,len(cipher),int(len(cipher)/inter)+1):
            elist.append(cipher[count:count+int(len(cipher)/inter)+1])
    else:
        for count in range(0,len(cipher),int(len(cipher)/inter)):
            elist.append(cipher[count:count+int(len(cipher)/inter)])
        
    # print(elist)

    for i in range(int(len(cipher)/inter)+1):
        for j in range(inter):
            try:
                new_str += elist[j][i]
            except Exception as e:
                pass

    print(new_str)
    return new_str


def rail_fence_encode_auto(message):
    """
    retrun 
    
    """
    e = message
    elen = len(e)
    field=[]
    for i in range(2,elen):
                if(elen%i==0):
                    field.append(i)
    for f in field:
        b = int(elen / f)
        result = {x:'' for x in range(b)}
        for i in range(elen):
            a = i % b;
            result.update({a:result[a] + e[i]})
        d = ''
        for i in range(b):
            d = d + result[i]
        print('分为\t'+str(f)+'\t'+'栏时，解密结果为：  '+d)
    




if __name__ == '__main__':
    rail_fence_encode('THERE IS A CIPHER',7)
    rail_fence_decode('TAHCEIRPEHIESR',7)
    rail_fence_encode('The quick brown fox jumps over the lazy dog',2)
    rail_fence_decode('Teucbonojmsvrhlzdghqikrwfxupoeteayo',2)
    rail_fence_encode_auto('TAHCEIRPEHIESR')