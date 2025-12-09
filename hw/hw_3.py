# Инкапсуляция
class Product:
    def __init__(self, name, price, discount=0):
        self.name = name
        self._price = price
        self.__discount = discount
    def get_price(self):
        final_price = self._price * (1 - self.__discount / 100)
        return final_price
    def set_discount(self, precent):
        if precent <= 50:
            self.__discount = precent
        else:
            return 'Скидка не может превышать 50%'
    def apply_extra_discount(self, code):
        if code == "VIP123":
            self.__discount += 5
            if self.__discount > 50:
                self.__discount = 50
        else:
            print ("Неверный код.")



p = Product("Iphone", 1000)

p.set_discount(20)
print("Цена со скидкой:", p.get_price())

p.apply_extra_discount("VIP123")
print("Цена после VIP:", p.get_price())

p.apply_extra_discount("wrong")
print("Цена итоговая:", p.get_price())

# Абстракция

from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    @abstractmethod
    def refund(self, amount):
        pass

class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата картой: {amount}")
    def refund(self, amount):
        print(f"Возврат средств: {amount}")
class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата наличными: {amount}")
    def refund(self, amount):
        print(f"Возврат наличных: {amount}")
class CryptoPayment(PaymentMethod):
    def pay(self, amount):
        print({"type": "crypto", "amount": amount, "currency": "USDT"})

    def refund(self, amount):
        print({"type": "crypto_refund", "amount": amount, "currency": "USDT"})

class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process(self, amount):
        self.payment_method.pay(amount)


processor = PaymentProcessor(CardPayment())
processor.process(100)

processor = PaymentProcessor(CashPayment())
processor.process(50)

processor = PaymentProcessor(CryptoPayment())
processor.process(200)
processor = PaymentProcessor(CryptoPayment())
processor.process(200)
