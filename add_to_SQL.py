import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Kết nối MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Đổi thành user của bạn
        password="123456",  # Đổi thành mật khẩu của bạn
        database="product_db"  # Đảm bảo đã tạo database này
    )

# Hàm lưu sản phẩm vào MySQL
def save_product():
    name = entry_name.get()
    price = entry_price.get()

    if name and price:
        try:
            db = connect_db()
            cursor = db.cursor()
            cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (name, price))
            db.commit()
            db.close()
            messagebox.showinfo("Thành công", "Sản phẩm đã được lưu!")
            entry_name.delete(0, tk.END)
            entry_price.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi lưu: {e}")
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập đủ thông tin!")

# Giao diện chính
def open_main():
    start_window.destroy()
    
    global entry_name, entry_price
    
    main_window = tk.Tk()
    main_window.title("Quản lý sản phẩm")
    
    tk.Label(main_window, text="Tên sản phẩm:").pack(pady=5)
    entry_name = tk.Entry(main_window)
    entry_name.pack(pady=5)
    
    tk.Label(main_window, text="Giá sản phẩm:").pack(pady=5)
    entry_price = tk.Entry(main_window)
    entry_price.pack(pady=5)
    
    tk.Button(main_window, text="Lưu", command=save_product).pack(pady=10)
    
    main_window.mainloop()

# Giao diện bắt đầu
start_window = tk.Tk()
start_window.title("Bắt đầu")

tk.Label(start_window, text="Chào mừng! Nhấn bắt đầu để vào hệ thống.").pack(pady=20)
tk.Button(start_window, text="Bắt đầu", command=open_main).pack()

start_window.mainloop()
##SQL_PVP and chatGPT
