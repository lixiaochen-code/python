# -*- coding: utf-8 -*-
# 转义字符

print("老师说：\"今天要收作业\"","打一个反斜杠\\")

# \n 换行     n ===> newline
print("hellow\nword")

# \t    一个tab键 位置   满四个键位·不够补够四个
print("0000\t0000")
print("00000\t0000")
print("000000\t0000")
print("0000000\t0000")

# \r    回车 会覆盖前面的内容
print("hellow\rword")

# \b    退格 会删除前面的一个字符
print("hellow\b")
print("测试汉字会不会退格\b")

# 原字符 不希望字符串中的转义字符起作用 就是在字符串之前加上 R 或者 r
print(r"hellow\nword!!!")
# print(r"hellow word\")  # 注意最后一个字符不能为反斜杠
print(r"https:\\www.baidu.com")
