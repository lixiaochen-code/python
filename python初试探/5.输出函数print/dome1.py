# -*- coding: utf-8 -*-
# 输出到控制台
print(3+1+9*2)
# 输出到文件内 1.所指定的盘符存在 2.要使用file=
fp=open("E:\learnWeb\python\python初试探/5.输出函数print\dome1.txt","a+") # a+的没有该文件 创建该文件 若是有 在后面追加内容
print("将内容输出到文件内,若是没有文件 将创建一个新的文件",file=fp)
fp.close()

# 不进行换行输出
print("a", "b", "c")

# 个人回顾 输出内容到.html文件内    *** 要使用file=
fps=open("E:\learnWeb\python\python初试探/5.输出函数print\dome1.html","a+")
print("<div id='dm' style='color:white;background:red; width:200px;height:200px'>你是猪2</div>",file=fps)
fps.close()