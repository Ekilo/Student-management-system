import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
import subprocess

# 读取xx.list文件内容
def read_list():
    data = []
    try:
        with open('data/xx.list', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                try:
                    # 手动处理每行数据，以逗号分隔键值对，并构建字典
                    item = {}
                    pairs = line.strip().split(', ')
                    for pair in pairs:
                        key, value = pair.split(': ')
                        item[key.strip()] = value.strip()
                    data.append(item)
                except Exception as e:
                    print(f"忽略格式错误的行: {line}")

    except FileNotFoundError:
        print("文件 'xx.list' 未找到")
    return data




# 创建信息编辑窗口
def create_info_edit_window(data):
    def submit_changes():
        # 获取当前所选项在树视图中的索引
        selected_item = tree.selection()[0]

        # 修改数据
        updated_data = {
            "姓名": labels[0]["text"],
            "年龄": labels[1]["text"],
            "性别": labels[2]["text"],
            "院校": labels[3]["text"],
            "专业": major_var.get()
        }

        # 更新树视图中的数据
        tree.item(selected_item, values=tuple(updated_data.values()))

        # 获取树视图中所有数据
        all_data = [tree.item(item)['values'] for item in tree.get_children()]

        # 更新文件内容
        with open('data/xx.list', 'w', encoding='utf-8') as file:
            for item in all_data:
                line = ', '.join([f"{key}: {value}" for key, value in zip(["姓名", "年龄", "性别", "院校", "专业"], item)])
                file.write(line + '\n')


        # 关闭信息编辑窗口
        edit_window.destroy()


    edit_window = tk.Toplevel()
    edit_window.title("信息编辑窗口")
    edit_window.geometry("446x546")

    # 显示信息
    labels = []

    for idx, label in enumerate(["姓名", "年龄", "性别", "院校"]):
        tk.Label(edit_window, text=label, font=("Arial", 12)).grid(row=idx, column=0, sticky="w")
        label_value = tk.Label(edit_window, text=data[label], font=("Arial", 12))
        label_value.grid(row=idx, column=1, sticky="w")
        labels.append(label_value)

    # 根据院校显示不同的专业选项
    majors = []
    if data["院校"] == "信息工程学院":
        majors = ["软件技术", "计算机应用", "人工智能"]
    elif data["院校"] == "影视学院":
        majors = ["视觉传播", "数字剪辑"]
    elif data["院校"] == "艺术学院":
        majors = ["舞蹈专业", "平面设计", "声乐专业"]

    if majors:
        tk.Label(edit_window, text="选择专业:", font=("Arial", 12)).grid(row=len(labels), column=0, sticky="w")
        major_var = tk.StringVar()
        major_var.set(majors[0])
        option_menu = tk.OptionMenu(edit_window, major_var, *majors)
        option_menu.grid(row=len(labels), column=1, sticky="w")

    # 添加提交按钮
    submit_button = tk.Button(edit_window, text="提交", command=submit_changes)
    submit_button.grid(row=len(labels) + 1, columnspan=2)

# 刷新列表
def refresh_list():
    # 这里使用示例数据代替
    data = read_list()
    # 清空现有列表
    for i in tree.get_children():
        tree.delete(i)
    # 读取并显示初始列表数据
    initial_data = read_list()
    for item in initial_data:
        tree.insert("", "end", values=tuple(item.values()))


# 搜索列表
def search_list():
    search_text = search_entry.get().lower()
    for item in tree.get_children():
        values = tree.item(item)['values']
        if search_text in str(values).lower():
            tree.selection_set(item)
        else:
            tree.selection_remove(item)

# 双击列表项事件
def on_double_click(event):
    item = tree.selection()[0]
    values = tree.item(item)['values']
    create_info_edit_window({key: value for key, value in zip(["姓名", "年龄", "性别", "院校", "专业"], values)})

def go_back():
    root.destroy()  # 关闭当前窗口
    subprocess.Popen(["python", "model/admin.py"])

# 设定字体样式和大小
button_font = ('Arial', 12)  # 修改字体为Arial，大小为12

# 创建主窗口
root = tk.Tk()
root.title("信息管理系统")
root.geometry("1280x720")

root.iconbitmap("icon.ico")

# 顶部搜索栏和按钮
search_frame = tk.Frame(root)
search_frame.pack(pady=20)

search_entry = tk.Entry(search_frame, width=50)
search_entry.pack(side=tk.LEFT, padx=10)

search_button = tk.Button(search_frame, text="搜索", command=search_list)
search_button.pack(side=tk.LEFT)

refresh_button = tk.Button(search_frame, text="刷新", command=refresh_list)
refresh_button.pack(side=tk.LEFT, padx=10)

# 创建返回按钮
back_button = tk.Button(root, text="返回登录", command=go_back,bg="lightcoral")
back_button.place(relx=0.8, rely=0.028)

# 创建列表
tree = tk.ttk.Treeview(root, columns=("姓名", "年龄", "性别", "院校", "专业"), show="headings", height=20)
tree.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# 设置列表宽度
tree.column("姓名", width=int(root.winfo_screenwidth() * 0.7 * 0.2))
tree.column("年龄", width=int(root.winfo_screenwidth() * 0.7 * 0.15))
tree.column("性别", width=int(root.winfo_screenwidth() * 0.7 * 0.15))
tree.column("院校", width=int(root.winfo_screenwidth() * 0.7 * 0.2))
tree.column("专业", width=int(root.winfo_screenwidth() * 0.7 * 0.2))

# 设置列表标题
tree.heading("姓名", text="姓名")
tree.heading("年龄", text="年龄")
tree.heading("性别", text="性别")
tree.heading("院校", text="院校")
tree.heading("专业", text="专业")

# 双击列表项事件绑定
tree.bind("<Double-1>", on_double_click)

# 读取并显示初始列表数据
initial_data = read_list()
for item in initial_data:
    tree.insert("", "end", values=tuple(item.values()))

root.mainloop()
