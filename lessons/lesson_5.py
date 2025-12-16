# Статический метод (@staticmethod)

class Math:
    def __init__(self, d, c):
        self.d = d
        self.c = c
    @staticmethod
    def add(a,b):
        return a + b

    @staticmethod
    def subtract(j , i):
        return j - i

# print(Math.add(12,12))
# print(Math.subtract(12, 1))
#  Можно вызвать через класс
#  Не зависит от объекта
#  Часто используется для утилитных функций

# 2. Метод класса (@classmethod)

class User:
    # Атрибуты класса
    default_role = "guest"

    def __init__(self, first_name, last_name):
        # Атрибуты экземпляра класса
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    @classmethod
    def create_from_name(cls, name):
        return cls(name, cls.default_role)

    @classmethod
    def get_base_role(cls):
        return cls.default_role

    # def get_name(self):
    #     return self.name

# Получает доступ к самому классу через cls.
# Используется для альтернативных конструкторов или работы с классом.

user_1 = User.create_from_name("User")
ardager = User("Ardager", "admin")

# print(user_1.role)
# print(ardager.role)


# 3. Декоратор @property
# Описание:
# Декоратор @property используется для того, чтобы метод стал доступным как атрибут, но при этом оставался методом.
# Это позволяет скрывать логику вычислений или проверки, делая код более чистым. Обычно используется
# для создания геттеров и сеттеров.


class Product:
    def __init__(self, name, price, full_info):
        self.name = name
        self.__price = price
        self.full_info = full_info
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("цена не может быть меньше 0")
        self.__price = value

    # @property
    # def full_info(self):
    #     return f"{self.name} {self.__price}"


iphone = Product('Iphone 17 pro max', 1200, "Iphone 17 pro max 1200")

# print(iphone.full_info)



# 1. Что такое декоратор?
# Декоратор — это функция, которая принимает другую функцию как аргумент и
# возвращает новую функцию, обычно обернутую в дополнительную функциональность.

def simple_decorator(func):
    def wrapper():
        print('До выполнения!!')
        func()
        print('После выполнения!!')
    return wrapper

@simple_decorator
def greeting():
    print("Hello world!!!")

# greeting()

def greeting_decorator(func):
    def wrapper(name):
        print(f"Привет {name}")
        func(name)
    return wrapper

@greeting_decorator
def greeting_name(name):
    print(f"Как дела {name}?")

# greeting_name("Ardager")

def repeat_decorator(n):
    def decorator(func):
        def wrapper(name):
            for i in range(n):
                func(name)
        return wrapper
    return decorator

@repeat_decorator(5)
def say_hello(name):
    print(f"привет {name}")

# say_hello("Ardager")


def class_decorator(cls):
    class NewClass(cls):
        def method(self):
            return "Я новый метод!!"
    return NewClass

@class_decorator
class OldClass:
    def method(self):
        return 'Я старый метод!!'

obj_1 = OldClass()
# print(obj_1.method())


def check_subscribe(func):
    def wrapper(user, comm):
        if user.subscribe in ["test", "test2"]:
            func(user, comm)
        else:
            print("вы не подписались на каналы!!")
    return wrapper

def is_admin_decorator(func):
    pass

# def permission_auth()
