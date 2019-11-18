import time

class Date:
    # Primary constructor:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


    # Alternative constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

if __name__ == "__main__":
    a = Date(2012, 12, 21)
    b = Date.today()

    # creating an instance without invoking init
    c = Date.__new__(Date)
    data = {"year": 2012, "month":8, "day":29}
    for key, value in data.items():
        setattr(c, key, value)
    print(c.year)
    print(c.month)
    print(c.day)
