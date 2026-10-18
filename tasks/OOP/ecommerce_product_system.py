from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, name, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")

        self.name = name
        self.price = price

    @abstractmethod
    def calculate_final_price(self):
        pass

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["price"])

    @staticmethod
    def is_valid_price(price):
        return isinstance(price, (int, float)) and not isinstance(price, bool) and price >= 0


class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)

        if not 0 <= discount <= 100:
            raise ValueError("Discount must be between 0 and 100.")

        self.discount = discount

    def calculate_final_price(self):
        return self.price * (1 - self.discount / 100)


def main():
    product_data = {
        "name": "Keyboard",
        "price": 100
    }

    product = DiscountedProduct.from_dict(
        {**product_data, "price": product_data["price"]},
        # Discount is supplied separately below.
    ) if False else DiscountedProduct(
        product_data["name"],
        product_data["price"],
        15
    )

    print(f"Product: {product.name}")
    print(f"Original price: ${product.price:.2f}")
    print(f"Discount: {product.discount}%")
    print(f"Final price: ${product.calculate_final_price():.2f}")
    print(f"Valid price: {Product.is_valid_price(product.price)}")


if __name__ == "__main__":
    main()
