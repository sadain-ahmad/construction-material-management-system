class Person:
    def __init__(self, cid, name, address, contact_number, email=None):
        self.__cid = cid
        self.__name = name
        self.__address = address
        self.__contact_number = contact_number
        self.__email = email

    # getter and setter for person id
    def get_cid(self):
        return self.__cid
    def set_cid(self, cid):
        self.__cid = cid

    # getter and setter for name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    # getter and setter for address
    def get_address(self):
        return self.__address
    def set_address(self, address):
        self.__address = address

    # getter and setter for contact number
    def get_contact_number(self):
        return self.__contact_number
    def set_contact_number(self, contact_number):
        self.__contact_number = contact_number

    # getter and setter for email
    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email

    def __str__(self):
        return f"CNIC: {self.__cid}\nName: {self.__name}\nAddress: {self.__address}\nContact Number: {self.__contact_number}\nEmail: {self.__email}"
    

class Supplier(Person):
    def __init__(self, cid, name, address, contact_number, email, factory_address):
        super().__init__(cid, name, address, contact_number, email)
        self.__factory_address = factory_address

    # getter and setter for factory address
    def get_factory_address(self):
        return self.__factory_address
    def set_factory_address(self, factory_address):
        self.__factory_address = factory_address

    def __str__(self):
        return super().__str__() + f"\nFactory Address: {self.__factory_address}"
    

class Builder(Person):
    def __init__(self, cid, name, address, contact_number, email, construction_site):
        super().__init__(cid, name, address, contact_number, email)
        self.__construction_site = construction_site

    # getter and setter for construction site
    def get_construction_site(self):
        return self.__construction_site
    def set_construction_site(self, site):
        self.__construction_site = site

    def __str__(self):
        return super().__str__() + f"\nConstruction Site: {self.__construction_site}"
    



class Client(Person):
    def __init__(self, cid, name, address, contact_number, supplier_id, builder_id, email=None):
        super().__init__(cid, name, address, contact_number, email)
        self.__supplier_id = supplier_id
        self.__builder_id = builder_id

    # getter and setter for supplier id
    def get_supplier_id(self):
        return self.__supplier_id
    def set_supplier_id(self, new_id):
        self.__supplier_id = new_id

    # getter and setter for builder id
    def get_builder_id(self):
        return self.__builder_id
    def set_builder_id(self, new_id):
        self.__builder_id = new_id

    def __str__(self):
        return super().__str__() + f"\nSupplier ID: {self.__supplier_id}\nBuilder ID: {self.__builder_id}"