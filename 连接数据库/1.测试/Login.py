# 导入 tkinter
from tkinter import *

# 创建窗口
win = Tk()
# 设置窗口标题
win.title("登录")
# 设置窗口标题
win.geometry("300x150")

# 将“账号”：“放置在x坐标为50，y坐标为30的位置”
Label(text='账号：').place(x=50, y=30)
# 创建一个用于输入账号的文本框，并且放置在界面上x = 100， y = 30 的位置
uname = Entry(win)
uname.place(x=100, y=30)
# 将“密码：”两个字防止子x = 50， y = 70 的位置
Label(text="密码：").place(x=50, y=70)
# 放置在x = 100, y = 70的位置
pwd = Entry(win)
pwd.place(x=100, y=70)

# 主循环，有了这行代码才可以持续的显示窗口
win.mainloop()
