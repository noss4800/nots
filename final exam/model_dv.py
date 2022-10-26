"""
Name: Chakan Wangboonkong
ID: 363411760001
Group: MIT431
"""

class Person:
    def __init__(self,name,age,email):
        self.__name = name
        self.__age = age
        self.__email = email

    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email

    def __str__(self):
        print(f'\tName: {self.__name}\n'
              f'\tAge: {self.__age}\n'
              f'\temail: {self.__email}\n')

class Student:
    def __init__(self,name,major,age,email):
        super().__init__(name,major,age,email)
        self.__id = id
        self.__major = major

    def get_id(self):
        return  self.__id
    def set_id(self,id):
        self.__id = id
    def get_major(self):
        return  self.__major
    def set_major(self,major):
        self.__major = major

    def __str__(self):
        print('Devices Report (Student):')
        super().__str__()
        print(f'\tSID: {self.__id}\n'
              f'\tMajor: {self.__major}\n')

class Employee:
    def __init__(self,name,position,age,email):
        super().__init__(name,position,age,email)
        self.__id = id
        self.__position = position

    def get_id(self):
        return  self.__id
    def set_id(self,id):
        self.__id = id
    def get_position(self):
        return  self.__position
    def set_position(self,position):
        self.__position = position
    def __str__(self):
        print('Employee Position (Employee):')
        super().__str__()
        print(f'\tEID: {self.__id}\n'
              f'\tposition: {self.__position}\n')

class Devices:
    def __init__(self, brand , model, price):
        self.__brand = brand #private member
        self.__model = model
        self.__price = price

    def devices_info(self):
        print(f'Brand: {self.__brand}' f'Model: {self.__model}' 
              f'Price: {self.__price}')

    def get_brand(self):
        return self.__brand
    def set_brand(self,brand):
        self.__brand = brand
    def get_model(self):
        return self.__model
    def set_model(self,model):
        self.__model = model
    def get_price(self):
        return self.__price
    def set_price(self,price):
        self.__price = price

class Mobile:
    def __init__(self,mobilebrand,model,price):
        self.__mobilebrand = mobilebrand
        self.__model = model
        self.__price = price

    def __str__(self):
        print(f'\tmobilebrand: {self.__mobilebrand}\n'
              f'\tmodel: {self.__model}\n'
              f'\tprice: {self.__price}\n')

class Tablet:
    def __init__(self,tebletbrand,model,price):
        self.__tebletbrand = tebletbrand
        self.__model = model
        self.__price = price

    def __str__(self):
        print(f'\ttebletbrand: {self.__tebletbrand}\n'
              f'\tmodel: {self.__model}\n'
              f'\tprice: {self.__price}\n')

class Labtop:
    def __init__(self,labtopbrand,model,price):
        self.__labtopbrand = labtopbrand
        self.__model = model
        self.__price = price

    def __str__(self):
        print(f'\tlabtopbrand: {self.__labtopbrand}\n'
              f'\tmodel: {self.__model}\n'
              f'\tprice: {self.__price}\n')

class DeviceReport:
    def __init__(self, owner):
        self.owner = owner
        self.device = list()

    def add_device(self, device):
        self.device = device

    def __str__(self):
        self.owner.__str__()
        for x in self.device:
            print(f'\tdevice {self.device.index(x) + 1}: {x[0].get_device()}  \t\tdate: {x[1]}')

print('Hello, from model.')