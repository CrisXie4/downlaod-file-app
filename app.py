import tkinter as tk
from tkinter import messagebox, filedialog
import requests
import os

def show_welcome():
    messagebox.showinfo("欢迎", "欢迎使用美美下载文件程序")

def download_file():
    url = url_entry.get()
    if not url.startswith("http"):
        messagebox.showerror("错误", "请输入有效的下载链接")
        return
    
    path = path_entry.get()
    if not path:
        path = filedialog.askdirectory(title="请选择下载路径")
        if not path:
            messagebox.showerror("错误", "未选择下载路径")
            return
        path_entry.delete(0, tk.END)
        path_entry.insert(0, path)
    
    try:
        response = requests.get(url, stream=True)
        filename = os.path.basename(url)
        filepath = os.path.join(path, filename)
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        messagebox.showinfo("成功", "文件下载完成")
    except Exception as e:
        messagebox.showerror("错误", f"下载失败：{str(e)}")

def change_path():
    path = filedialog.askdirectory(title="请选择下载路径")
    if path:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, path)

# 创建主窗口
root = tk.Tk()
root.title("美美下载文件程序")

# 显示欢迎弹窗
show_welcome()

# 创建输入框和标签
url_label = tk.Label(root, text="下载链接：")
url_label.grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

path_label = tk.Label(root, text="下载路径：")
path_label.grid(row=1, column=0, padx=10, pady=10)
path_entry = tk.Entry(root, width=50)
path_entry.grid(row=1, column=1, padx=10, pady=10)

# 创建按钮
download_button = tk.Button(root, text="开始下载", command=download_file)
download_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

change_path_button = tk.Button(root, text="更改路径", command=change_path)
change_path_button.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# 运行主循环
root.mainloop()