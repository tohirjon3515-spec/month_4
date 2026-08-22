class Date:
    """Sanani hisoblash klassi"""
    
    def __init__(self, day: int, month: int, year: int):
        # Shartlarni to'g'ri o'zgaruvchilarga bog'laymiz
        self.day = day if 1 <= day <= 31 else 0
        self.month = month if 1 <= month <= 12 else 0
        self.year = year if 1990 <= year <= 9999 else 0
        
    def getDay(self):
        return self.day
        
    def getMonth(self):
        return self.month
        
    def getYear(self):
        return self.year
        
    def setDay(self, d: int):
        if 1 <= d <= 31:
            self.day = d
            
    def setMonth(self, m: int):
        if 1 <= m <= 12:
            self.month = m
            
    def setYear(self, y: int):
        if 1990 <= y <= 9999:
            self.year = y
            
    def setDate(self, day: int, month: int, year: int):
        self.setDay(day)
        self.setMonth(month)
        self.setYear(year)
        
    def toString(self):
        # Kun va oyni chiroyli formatda (masalan, 08 shaklida) chiqarish uchun :02d ishlatsa bo'ladi
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

# Kodni tekshirish
date1 = Date(21, 8, 2026)
print(date1.toString())  # Natija: 21/08/2026
