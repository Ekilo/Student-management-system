import tkinter as tk
import subprocess  # 用于执行外部命令或程序

def open_search_module():
    root.destroy()
    subprocess.Popen(["python", "model/search_user.py"])

def go_back():
    root.destroy()  # 关闭当前窗口
    subprocess.Popen(["python", "main.py"])

# 创建主窗口
root = tk.Tk()
root.title("学生登录界面")
root.geometry("351x480")

root.iconbitmap("icon.ico")

# 设定字体样式和大小
button_font = ('Arial', 12)  # 修改字体为Arial，大小为12

site = 2

# 计算按钮的位置
button_width = 8 * site # 设置按钮宽度
button_height = 2 * site # 设置按钮高度

x_position = (351 - button_width) // 3  # 计算按钮横坐标居中
y_position = 20  # 计算按钮纵坐标靠上

add_label = tk.Label(root, text="点击查询可以查询信息", font=('Arial', 15), bg="#ADD8E6", fg="white")
add_label.place(relx=0.2, rely=0.1, anchor="w")

# 创建查询按钮
search_button = tk.Button(root, text="查询成绩", font=button_font, command=open_search_module, width=19, height=3)
search_button.place(relx=0.23, rely=0.3, anchor="w")

# 创建返回按钮
back_button = tk.Button(root, text="返回登录", font=button_font, command=go_back, width=19, height=3,bg="lightcoral")
back_button.place(relx=0.23, rely=0.6, anchor="w")

root.mainloop()