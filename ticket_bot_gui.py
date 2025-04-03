# # ticket_bot_gui.py

# import tkinter as tk
# from tkinter import ttk, messagebox
# import subprocess
# import json
# import os

# class TicketApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("搶票機器人")
#         self.root.geometry("400x600")

#         self.style = ttk.Style()

#         self.login_mode = tk.BooleanVar(value=False)
#         self.url_var = tk.StringVar()
#         self.username_var = tk.StringVar()
#         self.password_var = tk.StringVar()
#         self.target_time_var = tk.StringVar(value="2025-04-02 18:02:00")
#         self.theme_mode = tk.StringVar(value="自動")

#         self.price_vars = {i: tk.BooleanVar() for i in [1, 2, 3, 4]}
#         self.zone_vars = {zone: tk.BooleanVar() for zone in ["A", "B", "C"]}

#         self.build_ui()
#         self.apply_theme()

#     def build_ui(self):
#         theme_frame = tk.LabelFrame(self.root, text="顯示模式")
#         theme_frame.pack(pady=5, fill="x")
#         for mode in ["淺色", "深色", "自動"]:
#             tk.Radiobutton(theme_frame, text=mode, variable=self.theme_mode, value=mode, command=self.apply_theme, bg="black", fg="white").pack(side=tk.LEFT)

#         tk.Checkbutton(self.root, text="自動登入", variable=self.login_mode, bg="black", fg="white").pack(pady=5)

#         for label_text, var in [
#             ("目標網站", self.url_var),
#             ("帳號", self.username_var),
#             ("密碼", self.password_var),
#             ("搶票時間 (YYYY-MM-DD HH:MM:SS)", self.target_time_var)
#         ]:
#             tk.Label(self.root, text=label_text, bg="black", fg="white").pack()
#             tk.Entry(self.root, textvariable=var, show="*" if label_text == "密碼" else None, bg="gray20", fg="white", insertbackground="white").pack(pady=5, fill="x")

#         tk.Label(self.root, text="選擇價格類型", bg="black", fg="white").pack()
#         for i in self.price_vars:
#             tk.Checkbutton(self.root, text=f"類型 {i}", variable=self.price_vars[i], bg="black", fg="white").pack(anchor='w')

#         tk.Label(self.root, text="選擇區域", bg="black", fg="white").pack()
#         for z in self.zone_vars:
#             tk.Checkbutton(self.root, text=f"區域 {z}", variable=self.zone_vars[z], bg="black", fg="white").pack(anchor='w')

#         tk.Button(self.root, text="開始搶票", command=self.start_bot, bg="white", fg="black").pack(pady=10)

#     def apply_theme(self):
#         mode = self.theme_mode.get()
#         if mode == "深色":
#             self.root.configure(bg="black")
#         elif mode == "淺色":
#             self.root.configure(bg="white")
#         else:
#             pass  # 自動使用系統預設主題

#     def start_bot(self):
#         url = self.url_var.get().strip()
#         if not url:
#             messagebox.showerror("錯誤", "請輸入目標網站網址")
#             return

#         prices = [k for k, v in self.price_vars.items() if v.get()]
#         zones = [k for k, v in self.zone_vars.items() if v.get()]
#         target_time = self.target_time_var.get().strip()

#         payload = {
#             "login_mode": self.login_mode.get(),
#             "book_url": url,
#             "price_types": prices,
#             "zone_names": zones,
#             "username": self.username_var.get().strip(),
#             "password": self.password_var.get().strip(),
#             "target_time_str": target_time
#         }

#         with open("bot_args.json", "w", encoding="utf-8") as f:
#             json.dump(payload, f, ensure_ascii=False, indent=2)

#         subprocess.Popen([
#             os.environ.get("VENV_PATH", "python3"),
#             "ticket_bot_launcher.py"
#         ])

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = TicketApp(root)
#     root.mainloop()

# ticket_bot_gui.py

# ticket_bot_gui.py

import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import json
import os

class TicketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("搶票機器人")
        self.root.geometry("400x600")

        self.style = ttk.Style()

        self.login_mode = tk.BooleanVar(value=False)
        self.url_var = tk.StringVar()
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.target_time_var = tk.StringVar(value="2025-04-02 18:02:00")
        self.theme_mode = tk.StringVar(value="自動")

        self.price_vars = {i: tk.BooleanVar() for i in [1, 2, 3, 4]}
        self.zone_vars = {zone: tk.BooleanVar() for zone in ["A", "B", "C"]}

        self.label_refs = []
        self.entry_refs = []

        self.build_ui()
        self.apply_theme()

    def build_ui(self):
        theme_frame = tk.LabelFrame(self.root, text="顯示模式", bg="black", fg="white")
        theme_frame.pack(pady=5, fill="x")
        for mode in ["淺色", "深色", "自動"]:
            tk.Radiobutton(theme_frame, text=mode, variable=self.theme_mode, value=mode, command=self.apply_theme, bg="black", fg="white", selectcolor="gray20").pack(side=tk.LEFT)

        tk.Checkbutton(self.root, text="自動登入", variable=self.login_mode, bg="black", fg="white", selectcolor="gray20").pack(pady=5)

        # 修正 Label 和 Entry 的顯示
        fields = [
            ("目標網站", self.url_var),
            ("帳號", self.username_var),
            ("密碼", self.password_var),
            ("搶票時間 (YYYY-MM-DD HH:MM:SS)", self.target_time_var)
        ]

        for label_text, var in fields:
            label = tk.Label(self.root, text=label_text, bg="black", fg="white")
            label.pack(anchor="w", padx=10, pady=(5, 0))
            self.label_refs.append(label)

            entry = tk.Entry(self.root, textvariable=var, show="*" if label_text == "密碼" else None,
                             bg="gray20", fg="white", insertbackground="white", relief=tk.FLAT)
            entry.pack(fill="x", padx=10, pady=(0, 5))
            self.entry_refs.append(entry)

        tk.Label(self.root, text="選擇價格類型", bg="black", fg="white").pack(anchor="w", padx=10)
        for i in self.price_vars:
            tk.Checkbutton(self.root, text=f"類型 {i}", variable=self.price_vars[i], bg="black", fg="white", selectcolor="gray20").pack(anchor='w', padx=20)

        tk.Label(self.root, text="選擇區域", bg="black", fg="white").pack(anchor="w", padx=10)
        for z in self.zone_vars:
            tk.Checkbutton(self.root, text=f"區域 {z}", variable=self.zone_vars[z], bg="black", fg="white", selectcolor="gray20").pack(anchor='w', padx=20)

        tk.Button(self.root, text="開始搶票", command=self.start_bot, bg="white", fg="black").pack(pady=10)

    def apply_theme(self):
        mode = self.theme_mode.get()
        if mode == "深色":
            self.root.configure(bg="black")
            for label in self.label_refs:
                label.configure(bg="black", fg="white")
            for entry in self.entry_refs:
                entry.configure(bg="gray20", fg="white", insertbackground="white")
        elif mode == "淺色":
            self.root.configure(bg="white")
            for label in self.label_refs:
                label.configure(bg="white", fg="black")
            for entry in self.entry_refs:
                entry.configure(bg="white", fg="black", insertbackground="black")
        else:
            pass

    def start_bot(self):
        url = self.url_var.get().strip()
        if not url:
            messagebox.showerror("錯誤", "請輸入目標網站網址")
            return

        prices = [k for k, v in self.price_vars.items() if v.get()]
        zones = [k for k, v in self.zone_vars.items() if v.get()]
        target_time = self.target_time_var.get().strip()

        payload = {
            "login_mode": self.login_mode.get(),
            "book_url": url,
            "price_types": prices,
            "zone_names": zones,
            "username": self.username_var.get().strip(),
            "password": self.password_var.get().strip(),
            "target_time_str": target_time
        }

        with open("bot_args.json", "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

        subprocess.Popen([
            os.environ.get("VENV_PATH", "python3"),
            "ticket_bot_launcher.py"
        ])

if __name__ == "__main__":
    root = tk.Tk()
    app = TicketApp(root)
    root.mainloop()
