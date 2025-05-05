class Material:
    def __init__(self, cid, name, quantity, unit_price):
        self.__cid = cid
        self.__name = name
        self.__quantity = quantity
        self.__unit_price = unit_price

    # getter and setter for customer ID
    def get_cid(self):
        return self.__cid
    def set_cid(self, cid):
        self.__cid = cid

    # getter and setter for name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    # getter and setter for quantity
    def get_quantity(self):
        return self.__quantity
    def set_quantity(self, quantity):
        self.__quantity = quantity
    
    # getter and setter for unit price
    def get_unit_price(self):
        return self.__unit_price
    def set_unit_price(self, unit_price):
        self.__unit_price = unit_price

    # calculate total cost
    def total_cost(self):
        return self.__quantity * self.__unit_price
    
    def __str__(self):
        return f"Name: {self.__name}\nQuantity: {self.__quantity}\nUnit Price: {self.__unit_price}\nTotal Cost: {self.total_cost()}"



class RawMaterials(Material):
    def __init__(self, cid, name, quantity, unit_price):
        super().__init__(cid, name, quantity, unit_price)
        self.__category = "RAW"

    def get_category(self):
        return self.__category
    
    def __str__(self):
        return super().__str__()



class FinishingMaterials(Material):
    def __init__(self, cid, name, quantity, unit_price):
        super().__init__(cid, name, quantity, unit_price)
        self.__category = "FINISHING"
    
    def get_category(self):
        return self.__category
    
    def __str__(self):
        return super().__str__()
