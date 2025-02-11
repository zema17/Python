import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Kết nối MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="user_db"
)
cursor = conn.cursor()

# Hàm mở giao diện Đăng nhập / Đăng ký
def open_auth_screen():
    start_screen.destroy()  # Đóng cửa sổ bắt đầu
    auth_screen()  # Mở giao diện đăng nhập

# Hàm đăng ký tài khoản
def register():
    username = entry_username.get()
    password = entry_password.get()
    
    if username and password:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        messagebox.showinfo("Thành công", "Đăng ký thành công!")
    else:
        messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin")

# Hàm đăng nhập
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    
    if result:
        messagebox.showinfo("Thành công", "Đăng nhập thành công!")
    else:
        messagebox.showerror("Lỗi", "Tài khoản hoặc mật khẩu sai!")

# Giao diện Đăng nhập / Đăng ký
def auth_screen():
    global entry_username, entry_password
    
    auth = tk.Tk()
    auth.title("Đăng nhập / Đăng ký")

    tk.Label(auth, text="Username:").pack()
    entry_username = tk.Entry(auth)
    entry_username.pack()

    tk.Label(auth, text="Password:").pack()
    entry_password = tk.Entry(auth, show="*")
    entry_password.pack()

    tk.Button(auth, text="Đăng ký", command=register).pack()
    tk.Button(auth, text="Đăng nhập", command=login).pack()

    auth.mainloop()

# Giao diện bắt đầu
start_screen = tk.Tk()
start_screen.title("Giao diện tùy chỉnh")

start_button = tk.Button(start_screen, text="Bắt đầu", command=open_auth_screen, font=("Arial", 16), bg="orange")
start_button.pack(pady=50)

start_screen.mainloop()
