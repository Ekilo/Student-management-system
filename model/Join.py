import tkinter as tk
from tkinter import messagebox
import csv
import subprocess

def validate_input(P):
    return P.isalnum() or P == '_' or P == '-' or len(P) <= 20

def register():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if not (username.isalnum() or '_' in username or '-' in username) or len(username) > 20:
        messagebox.showerror("错误", "账号格式不符合要求")
        return
    if not (password.isalnum() or '_' in password or '-' in password) or len(password) > 20:
        messagebox.showerror("错误", "密码格式不符合要求")
        return

    if password != confirm_password:
        messagebox.showerror("错误", "确认密码与密码不一致")
        return

    # 检查用户名是否已存在于 CSV 文件中
    with open('data/log.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[1] == username:  # 检查用户名是否已存在
                messagebox.showerror("错误", "账号已存在")
                return

    # 将账号和密码写入 CSV 文件中并添加 'user' 标签
    with open('data/log.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['user', username, password])

    messagebox.showinfo("成功", "注册成功")

def go_back():
    root.destroy()  # 关闭当前窗口
    subprocess.Popen(["python", "main.py"])

root = tk.Tk()
root.title("注册用户")
root.geometry("351x400")

root.iconbitmap("icon.ico")

# 设定字体样式和大小
button_font = ('Arial', 12)  # 修改字体为Arial，大小为12

username_label = tk.Label(root, text="账号:")
username_label.pack()
validate_username = root.register(validate_input)
username_entry = tk.Entry(root, validate="key", validatecommand=(validate_username, '%P'))
username_entry.pack()

password_label = tk.Label(root, text="密码:")
password_label.pack()
password_entry = tk.Entry(root, show="*", validate="key", validatecommand=(validate_input, '%P'))
password_entry.pack()

confirm_password_label = tk.Label(root, text="确认密码:")
confirm_password_label.pack()
confirm_password_entry = tk.Entry(root, show="*", validate="key", validatecommand=(validate_input, '%P'))
confirm_password_entry.pack()

btn_width = len("".join(['账号:'] + [' '] * 20))
register_button = tk.Button(root, text="注册", command=register, width=btn_width)
register_button.place(relx=0.26, rely=0.38)

# 创建返回按钮
back_button = tk.Button(root, text="返回登录", command=go_back, width=btn_width,bg="lightcoral")
back_button.place(relx=0.26, rely=0.5)


root.mainloop()
