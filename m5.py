class Book:
    """Kitob haqida malumotlarni saqlovchi class"""
    def __init__(self, _id: int, title: str, author: str, price: float, quantity: float):
        self._id = _id
        self.title = title
        self.author = author
        self.price = price
        self.quatity = quantity
        
    def getID(self):
        return self._id
    def getTitle(self):
        return self.title
    def getAuthor(self):
        return self.author
    def getPrice(self):
        return self.price
    
    def setPrice(self, new_price: float):
        self.price = new_price
        
    def toString(self):
        return f"Book[id={self._id}, title={self.title}, author={self.author}, price={self.price}, quantity={self.quatity}]"
    
book1 = Book(123, "The Best Teacher", "Tokhirjon Makhmudov", 99.99, 777)
print(book1.toString())