maxNumber = int(input('请输入一个大于 2 的自然数:'))
lst = list(range(2, maxNumber))
# 最大整数的平方根
m = int(maxNumber ** 0.5)
for index, value in enumerate(lst):
    # 如果当前数字已大于最大整数的平方根，结束判断
    if value > m:
        break
    # 对该位置之后的元素进行过滤
    lst[index+1:] = filter(lambda x: x%value != 0, lst[index+1:])
print(lst)
