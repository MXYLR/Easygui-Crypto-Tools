#coding=utf-8
#!/usr/bin/env python3

from Caesar import *
from Vigenere import *
from easygui import *
from hill import *
import sys
import railFense

if __name__ == '__main__':
    while True:
        msgbox('Welcome to the cryptor tool', 'Made by  MXYLR')
        choice = choicebox(msg='Pick up a item', choices=['Caesar', 'Vigenere','Hill', 'Rail Fense'], title='MXYLR Crypto tools')

        if choice == 'Caesar':
            choiceCaesar = choicebox(msg='选择工作模式', choices=['Encrypt', 'Decrypt'], title='Caesar')
            if choiceCaesar == 'Encrypt':
                strs = enterbox(msg='输入明文序列 :', title='Caesar Encrypt tool')
                shift = int(enterbox(msg='偏移量 :'))
                C = caesar(strs, shift)
                msgbox(msg=C, title='密文')
            elif choiceCaesar=='Decrypt':
                CaesarP = enterbox(msg='输入密文序列 :', title='Caesar Decrypt tool')
                shift = int(enterbox(msg='偏移量 :'))
                msgbox(msg=caesarDecrypto(CaesarP, shift), title='明文 :')
            else:
                pass
        
        elif choice == 'Vigenere':
            choiceVigenere = choicebox(msg='选择工作模式', choices=['Encrypt', 'Decrypt'], title='Vigenere 维吉尼亚')
            if choiceVigenere == 'Encrypt':
                VigenereP = enterbox(msg='输入明文序列:', title='Vigenere Encrypt tool')
                VigenereK = enterbox(msg='输入密钥序列 :', title='Vigenere Encrypt tool')
                msgbox(msg=VigenereEncrypto(VigenereP, VigenereK), title='密文 :')
                pass
            elif choiceVigenere == 'Decrypt':
                VigenereP = enterbox(msg='输入密文序列 :', title='Vigenere Decrypt tool')
                VigenereK = enterbox(msg='输入密钥序列 :', title='Vigenere Decrypt tool')
                msgbox(msg=VigenereDecrypto(VigenereP, VigenereK), title='明文 :')
                pass
        elif choice == 'Hill':
            Hill_choice = choicebox(msg='选择工作模式', choices=['Encrypt', 'Decrypt'], title='Hill 希尔')
            if Hill_choice == 'Encrypt':
                msgbox('输入矩阵( shift + enter 换行 , 数字之间加空格)')
                matrix = inputMatrix()
                massage = enterbox(msg='输入明文序列 :', title='Hill Encrypt tool')
                massage = get_trim_text(massage)
                massageList = createMassageList(massage, matrix)
                ciphertextList = encrypt(massage, matrix)
                msgbox(msg=ciphertextList, title='密文')
            elif Hill_choice == 'Decrypt':
                massageList = list(map(int, list(enterbox(msg='输入密文序列(用逗号分隔) :').split(",")))) 
                msgbox(msg='输入矩阵( shift + enter 换行 , 数字之间加空格)')
                matrix = inputMatrix()
                matrix_inverse = createMatrixInverse(matrix)
                msgbox(msg='返回命令行查看逆矩阵')
                print("逆矩阵 :")
                for item in matrix_inverse:
                    print(item)
                plaintext = decrypt(massageList, matrix)
                msgbox(msg=plaintext, title='解密结果')
        elif choice == 'Rail Fense':
            railFense_choice = choicebox(msg='选择工作模式', choices=['Encrypt', 'Decrypt'], title='Rail Fense 栅栏密码')
            if railFense_choice == 'Encrypt':
                msgbox(msg=railFense.crypto(), title='密文')
            elif railFense_choice == 'Decrypt':
                msgbox(msg=railFense.decrypto(), title='解密结果')


        # 差一个列置换

        if ccbox('是否继续 ?', 'Its time to choose'):
            pass
        else:
            msgbox(msg='C.U.', ok_button='C.U.', title='See you f@cking next time')
            sys.exit(0)
    