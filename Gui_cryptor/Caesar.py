#coding=utf-8
#!/usr/bin/env python3

import Vigenere

#字符表
mstr = 'abcdefghijklmnopqrstuvwxyz'
#字符表长度
lengthM = len(mstr)

#strs为输入的明文，shitf为移动的位数
def caesar(strs, shift):
    strs = Vigenere.get_trim_text(strs)
    newstrs = ''
    for x in strs:
            #获取x字符在mstr中的位置
        numX = mstr.index(x)
        
            #新的字符位置加上shift
        numX = (numX + shift) % lengthM
        
        newstrs = newstrs + mstr[numX]
     
    return newstrs

# 解密， 移动的位数即为 shift 相反数
def caesarDecrypto(strs, shift):
    return caesar(strs, int(shift) * (-1));

if __name__ == '__main__':
    strs = input("Enter character sequence:")
    shift = int(input("Shift Numbers:"))
    C = caesar(strs, shift)
    print("CiperText:", C)
    print("PlainText:", caesarDecrypto(C, shift))