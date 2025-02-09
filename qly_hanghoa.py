class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.product_id}. {self.name} - {self.price}$ ({self.stock} còn lại)"

# Danh sách sản phẩm
products = []

# Nhập số lượng sản phẩm
num_products = int(input("Nhập số lượng sản phẩm: "))

# Nhập từng sản phẩm từ bàn phím
for i in range(num_products):
    print(f"Nhập thông tin cho sản phẩm {i + 1}:")
    name = input("Tên sản phẩm: ")
    price = float(input("Giá sản phẩm: "))
    stock = int(input("Số lượng: "))
    products.append(Product(i + 1, name, price, stock))

# Hiển thị danh sách sản phẩm sau khi nhập xong
print("\n📦 Danh sách sản phẩm:")
for product in products:
    print(product)
