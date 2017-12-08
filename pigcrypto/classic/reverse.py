#coding=utf-8

def reverse(message):
    '''
     reverse
     message  -> egassem
    '''
    # message = raw#! usr/bin/python

    translated = ''

    i = len(message) - 1
    while i >= 0:
        translated = translated + message[i]
        i = i-1

    print (translated)

# if __name__ == "__main__":
#     reverse('message')