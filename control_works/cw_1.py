from lessons.lesson_2 import MageHero


class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def action(self, name):
        return f"{name} готов к бою!"

class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super(). __init__(name, lvl, hp)
        self.mp = mp
    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"
class Warrior(MageHero):
    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"

class BankAccount:
    def __init__(self, hero, bank_name, balance, password):
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
        return f"Имя банка: {self.bank_name}"
    def bonus_for_level(self):
        self.hero.lvl *= 2
        return f"Бонус за уровень: 500 сом"
    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} сом"
    def __add__(self, other):
        if type(self) == type(other):
            total_balance = self._balance + other._balance
            print (f"Сумма счетов: {total_balance}")




