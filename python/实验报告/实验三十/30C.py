import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
 
matplotlib.rcParams['font.family'] = 'YouYuan'  # 幼圆字体
df = pd.read_csv('data.csv', encoding='936')  # 将csv文件读入DataFrame，并设置gbk编码
df = df.dropna()  # 删除所有缺失值，返回一个新的DataFrame
# 2）折线图，该饭店每天的营业额情况
df.plot(title='该饭店每天的营业额情况', xlabel='日期', ylabel='营业额')
# DataFrame的plot方法会在一个subplot中为各列绘制一条线，并自动创建图例
plt.savefig('first.jpg')
plt.clf()  # 清空当前figure
# 3）柱状图，显示每个月份的营业额
'''str.rfind()返回最后一个子字符串的第一个字符在str中的位置
Series的map方法可以接受一个函数或含有映射关系的字典型对象，这里传入函数，用x[:x.rfind('-')]保留年月'''
df['月份'] = df['日期'].map(lambda x: x[:x.rfind('-')])  # 添加一列'月份'
df_month = df.groupby('月份').sum()  # 按月份分组并求和，如果指定as_index=False则不以组标签为索引值
print(df_month)
df_month.plot.bar(title='该饭店每个月份的营业额', xlabel='月份', ylabel='营业额')  # df.plot(kind='bar')
plt.savefig('second.jpg')
plt.clf()
# 4）把涨幅最大的月份写入文件
# maxd = 0
# idx = 0
# for i in range(1, len(df_month['销量'])):
#     if maxd < df_month['销量'][i] - df_month['销量'][i - 1]:
#         maxd = df_month['销量'][i] - df_month['销量'][i - 1]
#         idx = i
df2 = df_month['销量'].diff()  # diff()计算Dataframe中某一元素与另一元素的差异(默认为前一行)
print(df2)
print(df2.nlargest(1))  # Dataframe.nlargest(n)返回按列降序的前n行
with open('maxMonth.txt', 'w') as fp:
    fp.write(df2.nlargest(1).keys()[0])  # keys()获取索引，第0号索引即月份
# 5）饼状图，四个季度的营业额分布情况
# y = [df_month[:3]['销量'].sum(), df_month[3:6]['销量'].sum(), df_month[6:9]['销量'].sum(), df_month[9:12]['销量'].sum()]
y = [df_month[3 * i:3 * i + 3]['销量'].sum() for i in range(4)]
plt.pie(y, labels=['第一季度', '第二季度', '第三季度', '第四季度'])
plt.savefig('third.jpg')
