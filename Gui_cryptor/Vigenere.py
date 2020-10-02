#coding=utf-8
#!/usr/bin/env python3

"""
Created on Nov 27 08:17:01 2018 at D704
@author: Kevil
"""
from string import ascii_lowercase as lowercase

# 加密, p 为明文， key 为密钥
def VigenereEncrypto(p, key):
    p = get_trim_text(p)
    ptLen = len(p)
    keyLen = len(key)

    quotient = ptLen // keyLen  # 商
    remainder = ptLen % keyLen  # 余

    out = ""
    for i in range(0, quotient):
        for j in range(0, keyLen):
            c = int((ord(p[i * keyLen + j]) - ord('a') + ord(key[j]) - ord('a')) % 26 + ord('a'))
            # global output
            out += chr(c)

    for i in range(0, remainder):
        c = int((ord(p[quotient * keyLen + i]) - ord('a') + ord(key[i]) - ord('a')) % 26 + ord('a'))
        # global output
        out += chr(c)

    return out

# 解密
def VigenereDecrypto(output, key):
    ptLen = len(output)
    keyLen = len(key)

    quotient = ptLen // keyLen
    remainder = ptLen % keyLen

    inp = ""

    for i in range(0, quotient):
        for j in range(0, keyLen):
            c = int((ord(output[i * keyLen + j]) - ord('a') - (ord(key[j]) - ord('a'))) % 26 + ord('a'))
            # global input
            inp += chr(c)

    for i in range(0, remainder):
        c = int((ord(output[quotient * keyLen + i]) - ord('a') - (ord(key[i]) - ord('a'))) % 26 + ord('a'))
        # global input
        inp += chr(c)

    return inp

def get_trim_text(text):
    text = text.lower()
    trim_text = ''
    for l in text:
        if lowercase.find(l) >= 0:
            trim_text += l
    return trim_text

if __name__ == '__main__':
    
        p = input("请输入明文: ")
        k = input("请输入密钥: ")
        print("加密后的密文是: %s" % (VigenereEncrypto(p, k)))
    
        c = VigenereEncrypto(p, k)
        print("解密后的明文是: %s" % (VigenereDecrypto(c, k)))