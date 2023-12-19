import tkinter as tk
import subprocess  # 用于执行外部命令或程序

def open_add_module():
    root.destroy()  # 关闭当前窗口
    subprocess.Popen(["python", "model/add.py"])

def open_search_module():
    root.destroy()  # 关闭当前窗口
    subprocess.Popen(["python", "model/search.py"])

def open_manage_module():
    root.destroy()  # 关闭当前窗口
    subprocess.Popen(["python", "model/manage.py"])

def go_back():
    root.destroy()  # 关闭当前窗口
    subprocess.Popen(["python", "main.py"])

# 创建主窗口
root = tk.Tk()
root.title("管理员界面")
root.geometry("351x600")

root.iconbitmap("icon.ico")

# 设定字体样式和大小
button_font = ('Arial', 12)  # 修改字体为Arial，大小为12

# 创建添加学生按钮
add_button = tk.Button(root, text="添加学生", font=button_font, command=open_add_module, width=19, height=3)
add_button.place(relx=0.2, rely=0.1, anchor="w")

# 添加按钮说明
add_label = tk.Label(root, text="点击添加学生信息", font=button_font)
add_label.place(relx=0.2, rely=0.1, anchor="w")

# 创建查询学生按钮
search_button = tk.Button(root, text="查询学生", font=button_font, command=open_search_module, width=19, height=3)
search_button.place(relx=0.2, rely=0.3, anchor="w")

# 添加按钮说明
search_label = tk.Label(root, text="点击以查询学生信息", font=button_font)
search_label.place(relx=0.2, rely=0.3, anchor="w")

# 创建编辑学生按钮
manage_button = tk.Button(root, text="编辑学生", font=button_font, command=open_manage_module, width=19, height=3)
manage_button.place(relx=0.2, rely=0.5, anchor="w")

# 添加按钮说明
manage_label = tk.Label(root, text="点击以编辑学生信息", font=button_font)
manage_label.place(relx=0.2, rely=0.5, anchor="w")

# 创建返回按钮
back_button = tk.Button(root, text="注销", font=button_font, command=go_back, width=19, height=3,bg="lightcoral")
back_button.place(relx=0.2, rely=0.8, anchor="w")

add_button.place_configure(relx=0.2, rely=0.1 + 0.1)
search_button.place_configure(relx=0.2, rely=0.3 + 0.1)
manage_button.place_configure(relx=0.2, rely=0.5 + 0.1)
back_button.place_configure(relx=0.2, rely=0.7 + 0.1)

root.mainloop()
