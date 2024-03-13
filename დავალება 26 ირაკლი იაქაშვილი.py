# 1.	მოცემულ კლასს მოარგე Single Responsibility პრინციპი და შესაბამისად შეცვალე კოდი. (კერძოდ დაშალე 4 კლასად User,  Storage,  HttpConnection,  Logger)
#
# class  User:
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def save(self):
#         ...
#
#     def send(self):
#         ...
#
#     def log(self):
#         ...
class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Storage:
    def save(self, user):
        print(f"Saving user {user.get_name()} to storage.")


class HttpConnection:
    def send(self, data):
        print(f"Sending data: {data}")


class Logger:
    def log(self, message):
        print(f"Logging: {message}")



if __name__ == "__main__":
    user = User("John Doe")
    storage = Storage()
    http_connection = HttpConnection()
    logger = Logger()

# 2.	მოცემული გვაქვს Discount კლასი.  Open-Closed პრინციპის გამოყენებით საჭიროა სწორად დავნერგოთ 40%_იანი ფასდაკლების ფუნქციონალი VIP კლიენტებისთვის.
# (შექმენი VIPDiscount კლასი)
#
# class Discount:
#   def __init__(self, customer, price):
#       self.customer = customer
#       self.price = price
#
#   def give_discount(self):
#       if self.customer == 'favourite':
#           return self.price * 0.2
#       if self.customer == 'vip':
#           return self.price * 0.4
#
from abc import ABC, abstractmethod


class User(ABC):

    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    @abstractmethod
    def discount(self):
        pass

class favourite_discount(User):
    def discount(self):
        if self.customer == 'favourite':
            return self.price * 0.2

class VIPDiscount(User):
    def discount(self):
        if self.customer == 'vip':
            return self.price * 0.4


user1 = favourite_discount("favourite", 50)
print(user1.discount())