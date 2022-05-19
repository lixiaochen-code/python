# 转义字符

# 换行字符  \n
print("hellow\nworld!!!")
# tab 以4为为一个集合 \t
print("hellow\twrold!!!")
# 退格 \r 回车 会覆盖掉前面的字符
print("hellow\rworld!!!")   # world将前面的hellow覆盖了
# 退一个格 \b   会删除前面的一个字符
print("hollow\bworld!!!")


# 转义字符 \
print('https://www.baidu.com')
print('\\\\')
print("老师说:'今天没有作业'")
print("老师说:\"今天没有作业\"")

# 原字符，不希望字符串上的转义字符起作用的字符，在 字符串 之前 加上 r 或 R
# 注意 最后一个字符不能是 一个\ 可以是\\
print(r"H\ne\rl\tl\bow World！！！")
# print(r"H\ne\rl\tl\bow World！！！\")        # 改行报错  不能为一个 \ 可以是两个 \
print(r"H\ne\rl\tl\bow World！！！\\")
