def toBinaryStr(x):#将有符号数x转换成二进制数
    if x>=0:#大于等于0的整数转换成二进制数
        out3='{0:08b}'.format(x)
        out4=out3.replace('0','-')
        return out4
    else:#负整数转换成二进制数
        x16=hex(x&0xFF)#将x转换成对于的十六进制数
        x10=int(x16,16)#将对应的十六进制数转换成十进制数
        out1=bin(x10)
        out2=out1[2:].replace('0','-')#字符串切片，截取掉前面的ob，字符串内建函数将截取后字符串里所有0替换成-
        return out2
#批量输入
str_in=input("Input：")      
strlist=str_in.split(' ')#字符串截取生成列表
i=1
for value in strlist:#遍历列表里每个元素
    if i%2!=0:
        x=value
    else:#将两个元素读取处理，再拼接打印
        y=value
        answer=toBinaryStr(int(x))+toBinaryStr(int(y))
        print(answer)
    i=i+1