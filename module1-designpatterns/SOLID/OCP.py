from abc import ABC, abstractmethod

class Discount(ABC):

    @abstractmethod
    def calculate(self, amount):
        pass


class StudentDiscount(Discount):

    def calculate(self, amount):
        return amount * 0.8


class EmployeeDiscount(Discount):

    def calculate(self, amount):
        return amount * 0.7


class VIPDiscount(Discount):

    def calculate(self, amount):
        return amount * 0.5


discount = VIPDiscount()

print(discount.calculate(1000))