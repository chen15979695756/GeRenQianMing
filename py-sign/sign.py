import re, requests
from tkinter import *
from PIL import ImageTk

def sign():
    url = 'http://www.uustv.com/'
    name = enter.get()
    if not name:
        messagebox.showinfo('提示：', '请输入您的名字')
    else:
        data = {
            'word': name,
            'sizes': 50,
            # 'fonts': 'jfcs.ttf',  # 个性签
            # 'fonts': 'qmt.ttf',  # 连笔签
            #'fonts': 'bzcs.ttf',  # 潇洒签
            # 'fonts': 'lfc.ttf',  # 草体签
            # 'fonts': 'haku.ttf',  # 合文签
            #'fonts': 'zql.ttf',  # 商务签
             'fonts': 'yqk.ttf',  # 可爱签
            'fontcolor': '#000000'
        }
        result = requests.post(url, data=data)
        result.encoding = 'utf-8'
        html = result.text
        reg = '<div class="tu">.*?<img src="(.*?)"/></div>'
        img_path = re.findall(reg, html)
        # 图片完整路径
        img_url = url + img_path[0]
        # 获取图片内容
        response = requests.get(img_url).content
        f = open('{}.gif'.format(name), 'wb')
        # 写入
        f.write(response)
        # 把图片放到窗口上，显示图片
        bm = ImageTk.PhotoImage(file='{}.gif'.format(name))
        label = Label(root, image=bm)
        label.bm = bm
        # 绘图
        label.grid(row=2, columnspan=2)

# 创建窗口
root = Tk()
# 标题
root.title('签名设计')
# 窗口大小
root.geometry('600x300')
# 窗口的初始位置
root.geometry('+400+200')
# 标签的控件
label = Label(root, text='输入名字', font=('宋体', 16), fg='blue')
label.grid()
# 输入框
enter = Entry(root, font=('宋体', 16))
# 设置输入框的位置
enter.grid(row=0, column=1)
# 按钮
button = Button(root, text='设计签名', font=('宋体', 16), command=sign)
# 设置按钮的位置
button.grid(row=1, column=0)
# 显示窗口
root.mainloop()