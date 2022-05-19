# -*- coding: utf-8 -*-
print("hollow world" "\n你是猪！！！")
print("你是互助")
print(10 * 20)
print(20)
# 可以输出字符串 数字 表达式
# 还可以把数据是出到文件中    注意点1.所指定的盘符存在 2要使用file
fp = open("./text.txt", "a+")
print("hollow world 增加文字aaa", file=fp);
fp.close()

# 若是不想进行换行输出  用,进行分割在一行内输出
print("hollow world", "不换行输出")

html = open("./text.html", "a+")
print("<div id='dm' style='color:white;background:red; width:200px;height:200px'>你是猪</div>", file=html);
html.close()
a = b = c = 1
print(a, b, c)
