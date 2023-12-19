import tkinter as tk
from tkinter import messagebox
import csv
import subprocess

def call_user_module():
    subprocess.Popen(["python", "model/user.py"], creationflags=subprocess.CREATE_NO_WINDOW)

def call_admin_module():
    subprocess.Popen(["python", "model/admin.py"], creationflags=subprocess.CREATE_NO_WINDOW)

def call_join_module():
    root.destroy()  # 关闭当前窗口
    subprocess.Popen(["python", "model/join.py"], creationflags=subprocess.CREATE_NO_WINDOW)

def read_log_list():
    data = []
    try:
        with open('data/log.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print("文件 'log.csv' 未找到")
    return data

def validate_input(P):
    return P.isalnum() or P == '_' or P == '-' or len(P) <= 20

def login():
    username = username_entry.get()
    password = password_entry.get()

    if not (username.isalnum() or '_' in username or '-' in username) or len(username) > 20:
        messagebox.showerror("错误", "账号格式不符合要求")
        return
    if not (password.isalnum() or '_' in password or '-' in password) or len(password) > 20:
        messagebox.showerror("错误", "密码格式不符合要求")
        return

    log_data = read_log_list()

    # 检查账号是否存在并调用相应的模块
    for row in log_data:
        if username == row[1] and password == row[2]:
            if row[0] == 'user':
                call_user_module()
            elif row[0] == 'admin':
                call_admin_module()
            root.destroy()  # 登录成功后关闭登录窗口
            return

    messagebox.showerror("错误", "账号不存在或密码错误")

root = tk.Tk()
root.title("学生管理系统登录")
root.geometry("351x400")

root.iconbitmap("icon.ico")

username_label = tk.Label(root, text="账号:")
username_label.pack()
validate_username = root.register(validate_input)
username_entry = tk.Entry(root, validate="key", validatecommand=(validate_username, '%P'))
username_entry.pack()

password_label = tk.Label(root, text="密码:")
password_label.pack()
validate_password = root.register(validate_input)
password_entry = tk.Entry(root, show="*", validate="key", validatecommand=(validate_password, '%P'))
password_entry.pack()

btn_width = len("".join(['账号:'] + [' '] * 20))
login_button = tk.Button(root, text="登录", command=login, width=btn_width)
login_button.pack()

join_button = tk.Button(root, text="注册", command=call_join_module, width=btn_width)
join_button.pack()

root.mainloop()
