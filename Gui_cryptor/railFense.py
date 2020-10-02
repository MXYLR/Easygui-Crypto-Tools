#coding=utf-8
#!/usr/bin/env python3


#栅栏密码加密解密
# @ChenYe 

from easygui import *

def crypto():
    plain = enterbox(msg='输入明文 :', title='Rail Fense 栅栏密码')
    n = int(enterbox(msg='输入每组字数', title='Rail Fense 栅栏密码'))
    ans = ''
    for i in range(n):
        for j in range(int(plain.__len__()/n + 0.5)):
            try:
                ans += plain[j*n+i]
            except:
                pass
    return ans
 
def decrypto():
    plain = enterbox(msg='输入密文 :', title='Rail Fense 栅栏密码')
    for n in range(2,plain.__len__()-1):
        ans = ''
        for i in range(n):
            for j in range(int(plain.__len__() / n + 0.5)):
                try:
                    ans += plain[j * n + i]
                except:
                    pass
        return ans
 
 
if __name__ == '__main__':
    msgbox(msg='栅栏密码加密/解密')
    while(True):
        choice = input('功能选择：\n1：加密\n2：解密\n')
        # 加密
        if choice == '1':
            msgbox(msg=crypto())
        # 解密
        elif choice == '2':
            msgbox(msg=decrypto())
        else:
            msgbox(msg='choice error!', title='ERROR')