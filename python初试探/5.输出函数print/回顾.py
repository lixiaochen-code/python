# -*- coding: utf-8 -*-
# 输出函数print 不换行输出
print("a","b","c")

# 把内容输入到文件内
fs=open("E:\learnWeb\python\python初试探/5.输出函数print/回顾.txt","a+") # a+ 是一种输出方式
print("输出内容到《回顾.txt》内 ，注意 要用 file=", file=fs)
fs.close()