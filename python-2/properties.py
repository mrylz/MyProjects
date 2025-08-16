class product:
    def __init__(self,name,price):
        self.name = name
        if price >= 0:
            self._price = price
        else:
            raise ValueError("Negatif değer girilemez")
        @property #  property sınıfı le bu şekilde erişimim kkısıtladık
        def price(self):
            return self._price
        @price.setter
        def price(self,value):
            if value >= 0:
                self._price = value
            else:
                raise  ValueError("Negatif değer girilemez")
p = product("iphone",16000) 
print(p.price)               