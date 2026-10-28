
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @staticmethod
    def is_valid_price(price):
        return isinstance(price, (int, float)) and not isinstance(price, bool) and price > 0

    def show_info(self):
        if not Product.is_valid_price(self.price):
            return "Invalid product price"

        return f"Product: {self.name}, Price: {self.price}"


print(Product.is_valid_price(150000))
print(Product.is_valid_price(-500))

product = Product("Keyboard", 150000)
print(product.show_info())
