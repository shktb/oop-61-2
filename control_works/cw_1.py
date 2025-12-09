class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def action(self):
        return f"{self.name} готов к бою!"

class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super(). __init__(name, lvl, hp)
        self.mp = mp
    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"

class WarriorHero(MageHero):
    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"

class BankAccount:
    def __init__(self, hero, balance, password, bank_name):
        self.hero = hero
        self.bank_name = bank_name
        self._balance = balance
        self.__password = password

    def login(self, password):
        if self.__password == password:
            return 'Пароль верный'
        else:
            return 'Пароль неверный!'

    def full_info(self):
        return f"{self.hero}, баланс: {self._balance}"

    def get_bank_name(self):
        return self.bank_name

    def bonus_for_level(self):
        self.hero.lvl *= 2
        return f"Бонус за уровень: 500 сом"


    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} сом"
    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            total_balance = self._balance + other._balance
            return f"Сумма счетов: {total_balance}"
        else:
            return "Ошибка! Нельзя складывать баланс разных классов"
    def __eq__(self, other):
        if self.hero.lvl == other.hero.lvl and self.hero.name == other.hero.name:
            return True
        else:
            return False



from abc import ABC, abstractmethod
class SMSService(ABC):
    @abstractmethod
    def send_otp(self, phone):
        pass
class KGSms(SMSService):
    def send_otp(self, phone):
        return f"<text>Код: 1234</text><phone>{phone}</phone>"

class RUSms(SMSService):
    def send_otp(self, phone):
        return {"text": "Код: 1234", "phone": f"{phone}"}



mage1 = MageHero("Merlin", 80, 500, 150)
mage2 = MageHero("Merlin", 80, 500, 200)
warrior = WarriorHero("Conan", 50, 900, 20)

acc1 = BankAccount(mage1, 5000, "1234", "Simba")
acc2 = BankAccount(mage2, 3000, "0000", "Simba")
acc3 = BankAccount(warrior, 2500, "1111", "Simba")

print(mage1.action())
print(warrior.action())

print(acc1)
print(acc2)

# --- Классовые и статические методы ---
print("Банк:", acc3.get_bank_name())
print(acc3.bonus_for_level())

# --- Магические методы: __add__ ---
print("\n=== Проверка __add__ ===")
print(acc1 + acc2)
print(acc1 + acc3)

# --- Магический метод: __eq__ ---
print("\n=== Проверка __eq__ ===")
print("Mage1 == Mage2 ?", acc1 == acc2)  # True — одинаковое имя и уровень
print("Mage1 == Warrior ?", acc1 == acc3)  # False

# --- SMS ---
sms = KGSms()
print("\n", sms.send_otp("+996777123456"))





