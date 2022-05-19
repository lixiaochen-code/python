import pymssql

# sql服务器名，这里(127.0.0.1)是本地数据库IP
serverName = '127.0.0.1'
# 登陆用户名和密码
userName = 'sa'
passWord = '0212'
# 建立连接并获取cursor
conn = pymssql.connect(serverName, userName, passWord, "carSales")
cursor = conn.cursor()
# 创建测试表 persons，包含字段：ID、name、salesrep
# cursor.execute("""
# IF OBJECT_ID('persons', 'U') IS NOT NULL
#     DROP TABLE persons
# CREATE TABLE persons (
#     id INT NOT NULL,
#     name VARCHAR(100),
#     salesrep VARCHAR(100),
#     PRIMARY KEY(id)
# )
# """)
# 插入三条测试数据
# cursor.executemany(
#     "INSERT INTO persons VALUES (%d, %s, %s)",
#     [(1, 'John Smith', 'John Doe'),
#      (2, 'Jane Doe', 'Joe Dog'),
#      (3, 'Mike T.', 'Sarah H.'),
#      (4, 'Li Chen', 'LIO')])
count = 0
sex = "男"
for i in "李赵王刘张肖石":
    for j in "晨辰大笑望杰":
        name = i + j
        place = j + i
        sql = "INSERT INTO persons VALUES(count, name, sex, place, '本科', 10000, 12345678910 , 4206822000021050+count + count)"
        cursor.execute(sql)
        count += 1
        print(count, i + j)
# 如果连接时没有设置autocommit为True的话，必须主动调用commit() 来保存更改。
conn.commit()
# cursor.execute('SELECT * FROM persons');
# 连接用完后记得关闭以释放资源
conn.close()