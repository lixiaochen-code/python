num = input('请输入一个自然数:')
print(sum(map(int, num)))

setA = eval(input('请输入一个集合:'))
setB = eval(input('再输入一个集合:'))
print('交集:', setA & setB)
print('并集:', setA | setB)
print('setA-setB:', setA - setB)

num = int(input('请输入一个自然数:'))
print('二进制:', bin(num)) 
print('八进制:', oct(num))
print('十六进制:', hex(num))
