import time

class Time:
    """Vaqtni boshqarish uchun klass"""
    def __init__(self, hour: int, minute: int, second: int):
        # Noto'g'ri vaqt berilsa, avtomatik 0 ga tenglaymiz
        self.hour = hour if 0 <= hour <= 23 else 0
        self.minute = minute if 0 <= minute <= 59 else 0
        self.second = second if 0 <= second <= 59 else 0
    
    def getHour(self):
        return self.hour
    
    def getMinute(self):
        return self.minute  # Xato tuzatildi: minut -> minute
    
    def getSecond(self):
        return self.second
    
    def setHour(self, h):
        if 0 <= h <= 23:
            self.hour = h
            
    def setMinute(self, m):
        if 0 <= m <= 59:
            self.minute = m
            
    def setSecond(self, s):
        if 0 <= s <= 59:
            self.second = s
        
    def setTime(self, hour: int, minute: int, second: int):
        self.setHour(hour)
        self.setMinute(minute)
        self.setSecond(second)
    
    def toString(self):
        # :02d - raqam 10 dan kichik bo'lsa, oldiga 0 qo'shib beradi (masalan: 05)
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
    
    def nextSecond(self):
        self.second += 1
        
        # Agar sekund 60 bo'lsa, uni 0 qilib, minutga 1 qo'shamiz
        if self.second == 60:
            self.second = 0
            self.minute += 1
            
            # Agar minut 60 bo'lsa, uni 0 qilib, soatga 1 qo'shamiz
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                
                # Agar soat 24 bo'lsa, yangi kun boshlanadi (0 bo'ladi)
                if self.hour == 24:
                    self.hour = 0
                    
        return self.toString()

    def previousSecond(self):
        self.second -= 1
        
        # Orqaga hisoblash mantig'i
        if self.second == -1:
            self.second = 59
            self.minute -= 1
            if self.minute == -1:
                self.minute = 59
                self.hour -= 1
                if self.hour == -1:
                    self.hour = 23
                    
        return self.toString()

# Soatni sinab ko'ramiz (kun tugashiga oz qolgan vaqt)
time1 = Time(23, 59, 55)

# 10 soniya davomida har soniyada vaqtni yangilab chiqaramiz
for i in range(10):
    print(time1.nextSecond(), end="\r", flush=True)
    time.sleep(1)
