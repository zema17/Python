import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# Kết nối MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Đổi thành user của bạn
        password="",  # Đổi thành mật khẩu của bạn
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
            load_products()  # Cập nhật danh sách
            entry_name.delete(0, tk.END)
            entry_price.delete(0, tk.END)
            messagebox.showinfo("Thành công", "Sản phẩm đã được lưu!")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi lưu: {e}")
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập đủ thông tin!")

# Hàm tải danh sách sản phẩm từ MySQL
def load_products():
    for row in tree.get_children():
        tree.delete(row)
    
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products")
    for product in cursor.fetchall():
        tree.insert("", "end", values=product)
    db.close()

# Hàm chọn sản phẩm để sửa
def select_product(event):
    selected = tree.focus()
    if selected:
        values = tree.item(selected, "values")
        entry_name.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        entry_name.insert(0, values[1])
        entry_price.insert(0, values[2])

# Hàm cập nhật sản phẩm
def update_product():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Cảnh báo", "Chọn một sản phẩm để cập nhật!")
        return

    values = tree.item(selected, "values")
    product_id = values[0]
    new_name = entry_name.get()
    new_price = entry_price.get()

    if new_name and new_price:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("UPDATE products SET name=%s, price=%s WHERE id=%s", (new_name, new_price, product_id))
        db.commit()
        db.close()
        load_products()
        messagebox.showinfo("Thành công", "Cập nhật sản phẩm thành công!")
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")

# Hàm xóa sản phẩm
def delete_product():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Cảnh báo", "Chọn một sản phẩm để xóa!")
        return

    values = tree.item(selected, "values")
    product_id = values[0]

    db = connect_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM products WHERE id=%s", (product_id,))
    db.commit()
    db.close()
    load_products()
    messagebox.showinfo("Thành công", "Xóa sản phẩm thành công!")

# Giao diện chính
root = tk.Tk()
root.title("Quản lý sản phẩm")

# Form nhập thông tin
tk.Label(root, text="Tên sản phẩm:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Giá sản phẩm:").grid(row=1, column=0, padx=5, pady=5)
entry_price = tk.Entry(root)
entry_price.grid(row=1, column=1, padx=5, pady=5)

# Các nút chức năng
tk.Button(root, text="Thêm", command=save_product).grid(row=2, column=0, pady=10)
tk.Button(root, text="Cập nhật", command=update_product).grid(row=2, column=1, pady=10)
tk.Button(root, text="Xóa", command=delete_product).grid(row=2, column=2, pady=10)

# Bảng hiển thị danh sách sản phẩm
columns = ("ID", "Tên", "Giá")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.grid(row=3, column=0, columnspan=3, padx=5, pady=5)
tree.bind("<<TreeviewSelect>>", select_product)

# Tải dữ liệu khi khởi động
load_products()

root.mainloop()
