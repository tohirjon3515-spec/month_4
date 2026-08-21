import time

class Time:
    """Vaqt"""
    def __init__(self, hour:int, minute:int, second:int):
        try:
            if 0 <= hour <= 23:
                self.hour = hour
            if 0 <= minute <= 59:
                self.minute = minute
            if 0 <= second <= 59:
                self.second = second
        except AttributeError:
            print("Xatolik!")
    
    def getHour(self):
        return self.hour
    def getMinute(self):
        return self.minute
    def getSecond(self):
        return self.second
    
    def setHour(self, h):
        self.hour = h
    def setMinute(self, m):
        self.minute = m
    def setSecond(self, s):
        self.second = s
        
    def setTime(self, hour:int, minute:int, second:int):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def toString(self):
        return f"{self.hour}:{self.minute}:{self.second}"
    def nextSecond(self):
        self.second += 1
        return f"{self.hour}:{self.minute}:{self.second+1}"
    def previousSecond(self):
        self.second -= 1
        return f"{self.hour}:{self.minute}:{self.second-1}"
    
time1 = Time(23, 15, 45)
# for i in range(1000):
#     print(time1.nextSecond())
#     time.sleep(1)
