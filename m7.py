class Market:
    """Bozordagi mahsulotlar kak Karzinka"""
    def __init__(self, name: str, address: str) -> None:
        self.name = name
        self.address = address
        self.products = {}
        self.balance = 0
        
    def get_products_info(self) -> str:
        print("Bozorda mavjud mahsulotlar:")
        if not self.products:
            print("Bozorda mahsulot mavjud emas")
            return
        for name, info in self.products.items():
            print(f"{name} - {info['price']} so'm, {info['quantity']} dona")
            
    def add_product(self, product: str, price: float, quantity: int) -> None:
        if product in self.products:
            self.products[product]["quantity"] += quantity
        else:
            self.products[product] = {"price": price, "quantity": quantity}
        
    def add_money(self, amount: float):
        self.balance += amount
        
    def remove_product(self, product: str) -> None:
        if product in self.products:
            self.products.pop(product)
            print(f"{product} mahsuloti o'chirildi.")
        else:
            print("Bunday mahsulot mavjud emas")

    def sell(self, product: str, quantity: int) -> None:
        if product not in self.products:
            print("Bunday mahsulot mavjud emas")
            return
        if self.products[product]["quantity"] < quantity:
            print("Yetarli mahsulot yo'q")
            return
        price = self.products[product]["price"]
        total = price * quantity
        self.products[product]["quantity"] -= quantity
        self.add_money(total)
        print(f"{quantity} dona {product} mahsuloti sotildi. Jami: {total} so'm")
        
bozor = Market(name="Supermarket", address="Toshkent, O'zbekiston")
bozor.add_product(product="Olma", price=5000, quantity=10)
bozor.add_product(product="Banan", price=7000, quantity=5)
bozor.get_products_info()
bozor.sell(product="Banan", quantity=3)
bozor.get_products_info()
bozor.remove_product(product="Banan")
bozor.get_products_info()
