class Car:
    """Avtomobil malumotlarini saqlovchi class"""
    def __init__(self, _id: int, brand: str, model: str, price: float, mileage: float, fuel: float):
        self._id = _id
        self.brand = brand
        self.model = model
        self.price = price
        self.mileage = mileage
        self.fuel = fuel
        
    def getBrand(self):
        return self.brand
    def getModel(self):
        return self.price
    def getPrice(self):
        return self.price

    def drive(self, distance):
        self.mileage += distance
        self.fuel -= distance * 0.1
        
    def refuel(self, amount):
        self.fuel += amount
        
    def toString(self):
        return f"Car[id={self._id}, brand={self.brand}, model={self.model}, price={self.price}, mileage={self.mileage} km, fuel={self.fuel} litr]"
    
car1 = Car(456, "Toyota", "Supra", 3000, 140000, 20)
print(car1.toString())
car1.drive(300)
print(car1.toString())
car1.refuel(40)
print(car1.toString())