import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

def fetch_article_data(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        )
    }
    resp = requests.get(url, headers=headers)
    # print(resp.content.decode())
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    script_tag = soup.select_one("script#lentille-context")
    if not script_tag:
        raise ValueError("没有找到 script#lentille-context 标签！")
    json_data = json.loads(script_tag.string)
    article = json_data["data"]["article"]
    title = article["title"]
    timestamp = int(article["time"])
    date = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
    pid = article.get("solutionFor", {}).get("pid", "unknown")
    problem_title = article.get("solutionFor", {}).get("title", "UnknownTitle")
    markdown = article["content"]
    return {
        "title": title,
        "date": date,
        "pid": pid,
        "problem_title": problem_title,
        "markdown": markdown
    }


def save_markdown(data, save_dir, tags, difficulty):
    os.makedirs(save_dir, exist_ok=True)
    pid_lower = data['pid'].lower()
    filepath = os.path.join(save_dir, f"{pid_lower}.md")
    difficulty_tag = difficulty.strip() if difficulty else ""
    full_title = f"[{difficulty_tag}] {data['pid']} {data['problem_title']}"
    short_title = f"[{difficulty_tag}] {data['pid']}"
    tag_string = "\n".join([f"    - {tag}" for tag in tags])
    frontmatter = f"""---\ntitle: "{full_title}"\nshortTitle: "{short_title}"\ndate: {data['date']}\ncategory: 做题笔记\ntag:\n{tag_string}\n---\n\n"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(frontmatter)
        f.write(data["markdown"])
    return filepath

# GUI 界面部分
def browse_dir():
    directory = filedialog.askdirectory()
    if directory:
        entry_dir.delete(0, tk.END)
        entry_dir.insert(0, directory)

def on_save():
    url = entry_url.get().strip()
    save_dir = entry_dir.get().strip()
    tag_input = entry_tag.get().strip()
    difficulty = entry_difficulty.get().strip()
    tags = [t.strip() for t in tag_input.replace(",", " ").split() if t.strip()]
    if not url or not save_dir:
        messagebox.showerror("错误", "请填写网址和目录！")
        return
    try:
        data = fetch_article_data(url)
        path = save_markdown(data, save_dir, tags, difficulty)
        messagebox.showinfo("成功", f"文章已保存到：{path}")
    except Exception as e:
        messagebox.showerror("失败", f"保存失败：{e}")

# 创建 GUI 窗口
root = tk.Tk()
root.attributes("-topmost", True)
root.title("题解文章保存工具")

tk.Label(root, text="文章网址：").grid(row=0, column=0, sticky="e")
entry_url = tk.Entry(root, width=50)
entry_url.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="保存目录：").grid(row=1, column=0, sticky="e")
entry_dir = tk.Entry(root, width=50)
entry_dir.grid(row=1, column=1, padx=5, pady=5)
btn_browse = tk.Button(root, text="浏览", command=browse_dir)
btn_browse.grid(row=1, column=2, padx=5)

tk.Label(root, text="难度（如Easy/1600）：").grid(row=2, column=0, sticky="e")
entry_difficulty = tk.Entry(root, width=50)
entry_difficulty.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="标签（可选）：").grid(row=3, column=0, sticky="e")
entry_tag = tk.Entry(root, width=50)
entry_tag.grid(row=3, column=1, padx=5, pady=5)

btn_save = tk.Button(root, text="保存文章", command=on_save, width=20)
btn_save.grid(row=4, column=1, pady=15)

root.mainloop()
