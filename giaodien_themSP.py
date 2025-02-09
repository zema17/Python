import tkinter as tk
from tkinter import messagebox

class ProductApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý Sản phẩm")

        # Danh sách sản phẩm
        self.products = []

        # Nhãn và ô nhập dữ liệu
        tk.Label(root, text="Tên sản phẩm:").grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(root, text="Giá:").grid(row=1, column=0)
        self.price_entry = tk.Entry(root)
        self.price_entry.grid(row=1, column=1)

        tk.Label(root, text="Số lượng:").grid(row=2, column=0)
        self.stock_entry = tk.Entry(root)
        self.stock_entry.grid(row=2, column=1)

        # Nút thêm sản phẩm
        self.add_button = tk.Button(root, text="Thêm sản phẩm", command=self.add_product)
        self.add_button.grid(row=3, columnspan=2)

        # Danh sách sản phẩm hiển thị
        self.product_list = tk.Listbox(root, width=40)
        self.product_list.grid(row=4, columnspan=2)

    def add_product(self):
        name = self.name_entry.get()
        price = self.price_entry.get()
        stock = self.stock_entry.get()

        if name and price.isdigit() and stock.isdigit():
            self.products.append(f"{name} - {price}$ ({stock} cái)")
            self.product_list.insert(tk.END, self.products[-1])
            self.clear_fields()
        else:
            messagebox.showerror("Lỗi", "Vui lòng nhập đúng thông tin!")

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.stock_entry.delete(0, tk.END)

# Chạy ứng dụng
root = tk.Tk()
app = ProductApp(root)
root.mainloop()
