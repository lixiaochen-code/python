"""
汽车销售管理系统功能
根据实验指导书要求，完成相关软件系统的设计，要求内容翔实，条理清晰，主要（关键代码）须有详细注释，
写清楚测试结果，并分析存在的问题：
1）能够实现汽车销售管理与相关信息的保存（到文件）和读取；
2）实现所有库存汽车相关信息的录入、显示、销售、修改等功能；
3）系统界面应类似下图所示的控制台界面（鼓励使用WEB或桌面窗体界面）：

其中，选择相应菜单代码之后进入相应的功能，可以：
1录入汽车信息（最后保存到文件）；
2显示已经保存的汽车信息（库存）；
3销售汽车：先显示已有汽车数据，选择销售的汽车编号之后将该车的信息删除；
4修改汽车信息，先通过编号选定汽车信息，然后更改；
5显示已经销售的汽车信息；
6退出。
"""


# 定义一个汽车类
class Cars(object):
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        info = "编号:%s\t汽车名称:%s\t\t价格:%d万元" % (self.id, self.name, self.price)
        return info


# 管理整个汽车商城的类
class ShopManager(object):

    def __init__(self, path):
        # path:表示读取文件的路径    shopdic：表示存放内存的容器
        self.path = path
        self.shopdic = self.readFileToDic()

    def readFileToDic(self):
        # 读取文件，写入到字典中
        f = open(self.path, 'r', encoding='utf-8')
        clist = f.readlines()
        f.close()
        index = 0
        shopdic = {}
        while index < len(clist):
            # 将每一行的字符串进行分割，存放到新的列表中
            ctlist = clist[index].replace('\n', "").split("|")
            # 将每行的内容存放到一个对象中
            car = Cars(ctlist[0], ctlist[1], int(ctlist[2]))
            # 将对向存放到集合中
            shopdic[car.id] = car
            index = index + 1
        return shopdic

    def writeContentFile(self):
        # 将内存当中的信息写入到文件当中
        str1 = ''
        for key in self.shopdic.keys():
            car = self.shopdic[key]
            ele = car.id + "|" + car.name + "|" + str(car.price) + "\n"
            # 拼接
            str1 = str1 + ele
        f = open(self.path, 'w', encoding='utf-8')
        f.write(str1)
        # 关闭文件
        f.close()

    def addCars(self):
        # 添加汽车的方法
        id = input("请输入添加汽车的编号:>")
        if self.shopdic.get(id):
            print("汽车编号已存在，请重新选择！")
            return
        name = input("请输入添加汽车名称:>")
        price = int(input("请输入添加汽车价格（万元）:>"))
        car = Cars(id, name, price)
        self.shopdic[id] = car
        print("添加成功！")

    def deleteCars(self):
        # 删除汽车的方法
        id = input("请输入删除汽车编号:>")
        if self.shopdic.get(id):
            del self.shopdic[id]
            print("删除成功！")
        else:
            print("汽车编号不存在！")

    def modCars(self):
        # 修改汽车的方法
        # 根据汽车的编号进行修改
        id = input("请输入要修改的汽车的编号")
        if self.shopdic.get(id):
            # 存在这个汽车编号才可以进行修改
            id1 = input("请输入修改后的汽车的编号:>")
            name1 = input("请输入修改后的汽车的名称：>")
            price1 = int(input("请输入修改后的汽车的价格（万元）:>"))
            car = Cars(id1, name1, price1)
            self.shopdic[id] = car
            print("修改成功！")
        else:
            print("汽车编号不存在")

    def showCars(self):
        # 展示所有汽车信息
        print("=" * 40)
        # 遍历
        for key in self.shopdic.keys():
            car = self.shopdic[key]
            print(car)
        print("=" * 40)

    def adminWork(self):
        info = """
        ==========欢迎进入购车商城==================
            输入功能编号，您可以选择以下功能：
            输入“1”：显示汽车的信息
            输入“2”：添加汽车的信息
            输入“3”：删除汽车的信息
            输入“4”：修改汽车的信息
            输入“5”：退出汽车系统功能
        ==========================================
        """
        print(info)
        while True:
            code = input("请输入功能编号:>")
            if code == "1":
                self.showCars()
            elif code == "2":
                self.addCars()
            elif code == "3":
                self.deleteCars()
            elif code == "4":
                self.modCars()
            elif code == "5":
                print("感谢您的使用，正在退出系统！！")
                self.writeContentFile()
                break
            else:
                print("输入编号有误，请重新输入！！")

    def userWork(self):
        print(" ==============欢迎进入购车商城==============")
        print("您可输入编号和购买数量选购汽车，输入编号为n则结账")
        self.showCars()
        total = 0
        while True:
            id = input("请输入购买商品编号:>")
            if id == "n":
                print("本次购买商品共消费%d万元，感谢您的光临！" % (total))
                break
            if self.shopdic.get(id):
                car = self.shopdic[id]
                num = int(input("请输入购买数量:>"))
                total = total + car.price * num
            else:
                print("输入商品编号有误，请核对后重新输入！")

    def login(self):
        # 登录功能
        print("==========欢迎登录购车商城===========")
        uname = input("请输入用户名:>> ")
        password = input("请输入密码:>> ")
        if uname == "admin":
            if password == "123456":
                print("欢迎您，admin管理员")
                self.adminWork()
            else:
                print("管理员密码错误，登录失败！")
        else:
            print("欢迎你，%s用户" % (uname))
            # 执行用户的购买功能
            self.userWork()


if __name__ == '__main__':
    shopManage = ShopManager("car.txt")
    shopManage.login()
