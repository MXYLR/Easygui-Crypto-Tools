#coding=utf-8
#!/usr/bin/env python3


'''
列置换密码
Auher：Jarrycow
time:2020-04-17
'''
import re

class colCode:
    __m=0
    __n=0
    __key=[] # 密钥
    __apaMsg="" # 明文
    __secMsg="" #密文
    
    def __init__(self,m): # 初始化，定义矩阵宽
        self.__m=m
        __n=0
        __key=[] 
        __apaMsg="" 
        __secMsg="" 
    def getKey(self,s): # 密钥形成函数
        m=self.__m
        Key={}
        antiKey={}
        s=re.split(r'[()]',s) #以()分界
        while '' in s: # 消除''
            s.remove('')
        temp=[]
        lenKey={i+1 for i in range(m)} #密钥长度
        for i in range(len(s)): 
            for j in range(len(s[i])-1):
                Key[int(s[i][j])]=int(s[i][j+1]) #密钥字典
                antiKey[int(s[i][j+1])]=int(s[i][j]) #反密钥字典
                temp.append(int(s[i][j])) #钥匙收录
            Key[int(s[i][-1])]=int(s[i][0]) #解决最后一个的问题
            antiKey[int(s[i][0])]=int(s[i][-1])
            temp.append(int(s[i][-1]))
        sameKey=lenKey-set(temp) #找到没有变化的密钥
        for i in sameKey:
            Key[i]=i
            antiKey[i]=i
        self.__key.append(Key)
        self.__key.append(antiKey)

    def enCode(self,p): #加密函数
        self.__apaMsg=p
        m=self.__m
        n=self.__n
        Key=self.__key[0]
        p=p.replace(' ','') #去除空格
        p+=' '*(m-len(p)%m) #末尾补齐
        n=len(p)//m #矩阵列数
        self.__n=n
        M=[p[i*m:(i+1)*m] for i in range(n)] #矩阵生成
        M=[M[i][Key[j+1]-1] for i in range(n) for j in range(m)] #矩阵转换
        M=''.join(M) #列表转换为字符串
        self.__secMsg=M
        return M
    
    def deCode(self,q):
        self.__apaMsg=p
        m=self.__m
        n=self.__n
        Key=self.__key[1]
        M=[q[i*m:(i+1)*m] for i in range(n)]
        M=[M[i][Key[j+1]-1] for i in range(n) for j in range(m)]
        M=''.join(M)
        self.__secMsg=M
        return M
    def Print(self):
        print(self.__m,self.__n,self.__key,self.__apaMsg,self.__secMsg)

if __name__=='__main__':
    m=6 #矩阵宽度
    p="Beijing 2008 Olympic Games"
    s='(143)(56)'
    a=colCode(m)
    a.getKey(s)
    q=a.enCode(p)
    e=a.deCode(q)
    a.Print()
def main():
    pass
