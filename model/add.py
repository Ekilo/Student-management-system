import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess

def on_school_select(*args):
    selected_school = school_var.get()

    if selected_school == "信息工程学院":
        majors = ["软件技术", "计算机应用", "人工智能"]
    elif selected_school == "影视学院":
        majors = ["视觉传播", "数字剪辑"]
    elif selected_school == "艺术学院":
        majors = ["舞蹈专业", "平面设计", "声乐专业"]
    else:
        majors = ["无"]

    # 更新专业选项框内容
    major_var.set("")  # 清空选项
    major_option['menu'].delete(0, 'end')
    for major in majors:
        major_option['menu'].add_command(label=major, command=tk._setit(major_var, major))

def validate_input():
    status_label.config(text="")  # 清空之前的错误提示

    name = name_entry.get()[:5]  # 获取姓名，限制长度为5个汉字以内
    age = age_entry.get()
    gender = gender_var.get()
    school = school_var.get()
    major = major_var.get()

    if not name:
        status_label.config(text="请输入有效的姓名")
    elif not age.isdigit() or int(age) >= 200:
        status_label.config(text="请输入有效的年龄")
    elif gender == "其它" and len(gender) > 36:
        status_label.config(text="性别选项超出长度限制")
    elif school == "无":
        status_label.config(text="请选择有效的院校")
    elif major == "无":
        status_label.config(text="请选择有效的专业")
    else:
        # 检查信息是否已存在
        with open("data/xx.list", "r", encoding="utf-8") as file:
            existing_info = file.readlines()
            new_info = f"姓名: {name}, 年龄: {age}, 性别: {gender}, 院校: {school}, 专业: {major}\n"

            if new_info in existing_info:
                status_label.config(text="该信息已存在，无需重复录入", fg="red")
                return

        # 将信息写入文件（指定编码为UTF-8）
        with open("data/xx.list", "a", encoding="utf-8") as file:
            file.write(new_info)
        status_label.config(text="信息已录入", fg="green")  # 提示录入成功

def go_back():
    root.destroy()  # 关闭当前窗口
    subprocess.Popen(["python", "model/admin.py"])

# 创建主窗口
root = tk.Tk()
root.title("学生信息添加")
root.geometry("449x622")

root.iconbitmap("icon.ico")

# 设定字体样式和大小
button_font = ('Arial', 12)  # 修改字体为Arial，大小为12

# 创建一个Frame来放置部件
main_frame = tk.Frame(root)
main_frame.pack(padx=50, pady=50)

name_label = tk.Label(main_frame, text="学生信息添加", font=("Arial", 14), anchor="center", bg="light blue", fg="white")
name_label.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

# 创建姓名标签和输入框
name_label = tk.Label(main_frame, text="姓名:", font=("Arial", 14), anchor="center", bg="light blue", fg="white")
name_label.grid(row=1, column=0, padx=20, pady=10, sticky=tk.W)

name_entry = ttk.Entry(main_frame)
name_entry.grid(row=1, column=1, padx=20, pady=10, sticky=tk.W)

age_label = tk.Label(main_frame, text="年龄:", font=("Arial", 14), anchor="center", bg="light blue", fg="white")
age_label.grid(row=2, column=0, padx=20, pady=10, sticky=tk.W)

age_entry = ttk.Entry(main_frame)
age_entry.grid(row=2, column=1, padx=20, pady=10, sticky=tk.W)

gender_label = tk.Label(main_frame, text="性别:", font=("Arial", 14), anchor="center", bg="light blue", fg="white")
gender_label.grid(row=3, column=0, padx=20, pady=10, sticky=tk.W)

gender_var = tk.StringVar(root)
gender_var.set(" ")  # 默认选项
gender_option = tk.OptionMenu(main_frame, gender_var, "男", "女",)
gender_option.grid(row=3, column=1, padx=20, pady=10, sticky=tk.W)

school_label = tk.Label(main_frame, text="院校:", font=("Arial", 14), anchor="center", bg="light blue", fg="white")
school_label.grid(row=4, column=0, padx=20, pady=10, sticky=tk.W)

schools = ["信息工程学院", "影视学院", "艺术学院"]  # 更新院校选项
school_var = tk.StringVar(root)
school_var.set(" ")  # 默认选项
school_option = tk.OptionMenu(main_frame, school_var, *schools)
school_option.grid(row=4, column=1, padx=20, pady=10, sticky=tk.W)
school_var.trace('w', on_school_select)  # 追踪院校选项变化

major_label = tk.Label(main_frame, text="专业:", font=("Arial", 14), anchor="center", bg="light blue", fg="white")
major_label.grid(row=5, column=0, padx=20, pady=10, sticky=tk.W)

majors = [" "]  # 初始专业选项
major_var = tk.StringVar(root)
major_var.set(" ")  # 默认选项
major_option = tk.OptionMenu(main_frame, major_var, *majors)
major_option.grid(row=5, column=1, padx=20, pady=10, sticky=tk.W)

status_label = tk.Label(main_frame, text="", fg="red")
status_label.grid(row=6, columnspan=2, padx=20, pady=10, sticky=tk.W)

# 创建录入按钮
submit_button = tk.Button(main_frame, text="录入", font=("Arial", 12), command=validate_input)
submit_button.grid(row=7, column=0, columnspan=2, padx=20, pady=10, sticky=tk.E + tk.W)

# 创建返回按钮
back_button = tk.Button(root, text="返回", font=button_font, command=go_back, width=19, height=3, bg="lightcoral")
back_button.place(relx=0.3, rely=0.8, anchor="w")

root.mainloop()
