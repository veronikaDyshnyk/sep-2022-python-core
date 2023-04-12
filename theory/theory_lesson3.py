# так виглядає клас
class User:
    # можна працювати тільки з полями в казаними тут + для економії памяті
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        # модифікатори доступу питу __private _protected
        self.name = name
        self.age = age

    # перегрузка (перевизначення метода) типу як то стрінг в джаві
    def __str__(self):
        return f'{self.name}, {self.age}'


# екземпляр класу
user = User('max', 22)

print(user)


# наслідування

class User2(User):
    def __init__(self, name, age):
        super().__init__(name, age)


# можливе множинне наслідування і тоді в клак який наслідує передається конструктор тільки першого класу
class Car:
    def __init__(self, brand):
        self.brand = brand


class Greeting:
    def greeting(self):
        print('hello')


class MyCar(Car, Greeting):
    def __init__(self, brand, seats):
        super().__init__(brand)
        self.seats = seats


# car = MyCar('volvo', 4)
# car.greeting()


# інкапсуляція
class User3:
    def __init__(self, name):
        self.__name = name

    def __get_name(self):
        return self.__name

    def __set_name(self, new_name):
        if new_name != 'thir':
            self.__name = new_name

    def __del_name(self):
        del self.__name

    name = property(fset=__set_name, fget=__get_name, fdel=__del_name)


# us = User3('ika')
# print(us.name)
# us.name = 'kira'
# print(us.name)
# del us.name
# print(us.name)

# але це не дуже клаcний спосід тому придували "надбудову"^property
# u = User3('mika')
#
# print(u.get_name())
# u.set_name('fika')
# print(u.get_name())
# u.del_name()
# але і цей варіан громісткий тому є простіший--->
# class User4:
#     def __init__(self, name):
#         self.__name = name
#
# #над змінною яка щось повертає ставимо декоратор property
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         if new_name != 'thir':
#             self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         del self.__name

# поліморфізм

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return self.a * self.b / self.c

    def perimetr(self):
        return self.a + self.b + self.c


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimetr(self):
        return (self.a + self.b) * 2


#
# # в цьому варіанті є мінус: в класах нащадках не обовязково перевизначати методт що може привести до помилок

# тому треба додати абстракність і тоді мусимо імпленентувати всі методи інакще буде давати помилку^

# shapes = [Triangle(2, 2, 3), Rectangle(2, 2), Triangle(2, 3, 2)]
# shapes: list[Shape] = [Triangle(2, 2, 3), Rectangle(2, 2), Triangle(2, 3, 2)]
#
# for shape in shapes:
#     print(shape.area())
#     print(shape.perimetr())

##додаткові докоратори static, class method


# час 54хв


class UserN:
    __count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # static - не використовує екземпляри класу або будьякі параметри нашого класу
    @staticmethod
    def greeting():
        print('Hello')

    # classmethod - позначає мотоди які використовують звернення до самого класу (cls = назва класу)
    @classmethod
    def get_count(cls):
        print(cls.__count)

    @classmethod
    def inc_count(cls):
        cls.__count += 1


# і клас метод вікликається від самого класу а не від екземпляру

# user_n = UserN('name', 24)
# # user_n.greeting()
# # user_n.get_count()
# # user_n.inc_count()
# # user_n.get_count()
# UserN.get_count()
# UserN.inc_count()
# UserN.get_count()

# ----------------перегрузка мотодів
# ----singleton


class UserSingle:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name, age):
        self.name = name
        self.age = age


# отже від такого класу можна створити тільки один екземпляр, якщо спробуємо створити ще один, то в них буде
# одне і теж посилання і ід, а також якщо дані в другому будуть інакші, то вони перезапишуться і в першому


# можемо заставити екземпляр класу бути функцією


# class A:
#     def __init__(self, value):
#         self.value = value
## метод будує поведінку екземплярів класу
#     def __call__(self, inc):
#         return self.value + inc
#
#
# a = A(5)
# print(a(4))
# print(a.value)

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.__dict__}'  # dict представлення в словниковому варіанті

    def __repr__(self):  # репрезентація
        return f'{self.__dict__}'  # якщо в нас є список одєктів

    def __len__(self):  # можна навчити рахувати щось, тут довжину імені
        return len(self.name)

    def __add__(self, other):  # можна навчити додавати щось
        return self.age + other.age

    def __sub__(self, other):  # ---- "якісь чинники"
        return self.age * other.age

    def __mul__(self, other):
        return self.age * other.age

    def __lt__(self, other):  # ---lt< lte>= gt> gte>=
        return len(self.name) < len(other.name)

#
# human1 = Human('niko', 24)
# human2 = Human('kate', 22)
# print(human1)
#
# print([human1, Human('kate', 22)])
# print(human1 + human2)
# print(human1 - human2)
# print(human1 * human2)
# print(human1 < human2)

# по суті ми описуємо дію/реакцію на якісь чинники, а репрезентацію можемо дати свою
# як тут кажемо відніми юзерів і реакція поремножити вік


## власний тип

