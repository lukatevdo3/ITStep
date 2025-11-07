class Product:
    def __init__(self, price):
        self.__price = price
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self,value):
        if type(value) not in (int, float) or value <0:
            return ValueError("Price Should Be Positive number!")
        
        self.__price = value

    



p = Product(50)
print(f"საქონლის ფასი: {p.price} ლარი")