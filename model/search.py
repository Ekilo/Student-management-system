import tkinter as tk
from tkinter import messagebox
import subprocess

def update_major_options(*args):
    selected_school = school_var.get()

    if selected_school == "信息工程学院":
        majors = ["软件技术", "计算机应用", "人工智能"]
    elif selected_school == "影视学院":
        majors = ["视觉传播", "数字剪辑"]
    elif selected_school == "艺术学院":
        majors = ["舞蹈专业", "平面设计", "声乐专业"]
    else:
        majors = []

    # 更新专业选项框内容
    major_var.set("")  # 清空选项
    major_option['menu'].delete(0, 'end')
    for major in majors:
        major_option['menu'].add_command(label=major, command=tk._setit(major_var, major))

def search_student():
    # 获取输入值
    school = school_var.get()
    major = major_var.get()
    name = name_entry.get()

    # 非空检查
    if school == "":
        messagebox.showerror("错误", "院校不能为空")
        return
    if major == "":
        messagebox.showerror("错误", "专业不能为空")
        return

    # 读取文件并查询
    found = False
    with open("data/xx.list", "r", encoding="utf-8") as file:
        for line in file:
            info = line.strip().split(", ")
            if school == info[3][4:] and major == info[4][4:] and name == info[0][4:]:
                results_text.insert(tk.END, line + "\n")
                found = True

    # 若未找到则显示提示信息
    if not found:
        current_text = results_text.get("1.0", tk.END)
        if "未找到该学生，请重新查询" in current_text:
            results_text.delete("1.0", "end-1c")  # 删除指定的提示信息
        else:
            messagebox.showinfo("提示", "未找到该学生，请重新查询")

def go_back():
    root.destroy()  # 关闭当前窗口
    subprocess.Popen(["python", "model/admin.py"])

# 创建主窗口
root = tk.Tk()
root.title("学生信息查询")
root.geometry("606x655")

root.iconbitmap("icon.ico")

# 设定字体样式和大小
button_font = ('Arial', 12)  # 修改字体为Arial，大小为12

# 创建输入框和标签
school_label = tk.Label(root, text="院校:")
school_label.pack()

schools = ["信息工程学院", "影视学院", "艺术学院"]  # 院校选项
school_var = tk.StringVar(root)
school_var.set("信息工程学院")  # 默认选项
school_option = tk.OptionMenu(root, school_var, *schools, command=update_major_options)
school_option.pack()

major_label = tk.Label(root, text="专业:")
major_label.pack()

major_var = tk.StringVar(root, "")  # 默认选项
major_option = tk.OptionMenu(root, major_var, "")  # 初始创建OptionMenu
major_option.pack()

name_label = tk.Label(root, text="姓名:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

search_button = tk.Button(root, text="查询", command=search_student)
search_button.pack()

results_text = tk.Text(root, height=20, width=80)
results_text.pack()

# 创建返回按钮
back_button = tk.Button(root, text="返回", font=button_font, command=go_back, width=19, height=3,bg="lightcoral")
back_button.place(relx=0.35, rely=0.8, anchor="w")

root.mainloop()
