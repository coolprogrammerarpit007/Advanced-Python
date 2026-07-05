class Device:
    def __init__(self,brand):
        self._brand = brand

    @property
    def brand(self):
        return f"Brand Name is: {self._brand}"

    @brand.setter
    def brand(self,value):
        self._brand = value

    def power_on(self):
        return f"{self._brand} device is now powered ON."


class SmartDevice(Device):
    def __init__(self,brand,connectivity):
        super().__init__(brand)
        self.connectivity = connectivity


    def show_status(self):
        return f"{self.brand} {'connected' if self.connectivity else 'not connected'} to the Internet."


class DeviceCamera(SmartDevice):
    def __init__(self,brand,connectivity,resolution):
        super().__init__(brand,connectivity)
        self.resolution = resolution


    def record(self):
        return f"Recording video at {self.resolution} pixel resolution"



phone = DeviceCamera("Samsung",True,2048)
# print(phone.record())
# print(phone.show_status())
# print(phone.brand)
phone.brand = "Apple Iphone"
# print(phone.brand)


# In Python, Method Resolution Order (MRO) is the specific order in which a programming language searches for a method or attribute in a class hierarchy.Python uses an algorithm called C3 Linearization to determine this order, which ensures that a class always appears before its parents and that the order of multiple base classes is preserved.

class A:
    def greet(self):
        print("Hello From Class A")


class B(A):
    def greet(self):
        print("Hello From Class B")

class C(A):
    def greet(self):
        print("Hello From Class C")

class D(B,C):
    pass


obj = D()
# obj.greet()



# Polymorphism

class CreditCard:
    def process_payment(self,amount):
        return f"Charging amount: {amount}$ from your credit card."



class Paypal:
    def process_payment(self,amount):
        return f"Redirecting your Paypal wallet to charge ${amount} from your wallet."



def checkout_payment(payment_gateway,amount):
    print(payment_gateway.process_payment(amount))



credit_card = CreditCard()
paypal = Paypal()

checkout_payment(credit_card,500)
checkout_payment(paypal,750)
