# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін

class Rectangle:
    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y
        self.area = x * y

    def __add__(self, other: 'Rectangle') -> int:
        return self.area + other.area

    def __sub__(self, other: 'Rectangle') -> int:
        return self.area - other.area

    def __eq__(self, other: 'Rectangle') -> bool:
        return self.area == other.area

    def __ne__(self, other: 'Rectangle') -> bool:
        return self.area != other.area

    def __lt__(self, other: 'Rectangle') -> bool:
        return self.area < other.area

    def __gt__(self, other: 'Rectangle') -> bool:
        return self.area > other.area

    def __len__(self) -> int:
        return (self.__x + self.__y) * 2


###############################################################################

# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір ноги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок,
# та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів класу
# також має бути метод класу, який буде виводити це значення

class Human:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age


class Cinderella(Human):
    __count = 0

    def __init__(self, name: str, age: int, shoe_size: int) -> None:
        super().__init__(name, age)
        self.shoe_size = shoe_size
        Cinderella.__count += 1

    def __str__(self) -> str:
        return str(self.__dict__)

    @classmethod
    def show_count(cls) -> None:
        print(cls.__count)


class Prince(Human):
    def __init__(self, name: str, age: int, found_shoe: int) -> None:
        super().__init__(name, age)
        self.__found_shoe = found_shoe

    def find_cinderella(self, cinderellas: list[Cinderella]) -> None:
        for cinderella in cinderellas:
            if self.__found_shoe == cinderella.shoe_size:
                print(cinderella)
                break


cinderellas_list: list[Cinderella] = [
    Cinderella('Viky', 20, 36),
    Cinderella('Miky', 21, 33),
    Cinderella('iky', 20, 39),
    Cinderella('Bob', 25, 45)
]

prince = Prince('Max', 20, 33)

prince.find_cinderella(cinderellas_list)
Cinderella.show_count()
###############################################################################
#
# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають
# є класом Book або Magazine інакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного класу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного класу

from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self) -> None:
        pass


class Book(Printable):
    def __init__(self, name: str) -> None:
        self.__name = name

    def print(self):
        print(f'{self.__class__.__name__} - {self.__name}')


class Magazine(Printable):

    def __init__(self, name: str) -> None:
        self.__name = name

    def print(self) -> None:
        print(f'{self.__class__.__name__} - {self.__name}')


class Main:
    __printable_list: list[Book | Magazine] = []

    @classmethod
    def add(cls, item: Book | Magazine) -> None:
        # if isinstance(item, Magazine) or isinstance(item, Book):
        if isinstance(item, (Magazine, Book)):
            cls.__printable_list.append(item)

    @classmethod
    def show_all_magazines(cls) -> None:
        for item in cls.__printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls) -> None:
        for item in cls.__printable_list:
            if isinstance(item, Book):
                item.print()


Main.add(Magazine('vogue'))
Main.add(Magazine('zara'))
Main.add(Book('flowers'))
Main.add(Book('die young'))

Main.show_all_books()
Main.show_all_magazines()
# Приклад:
#
# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()

# для перевірки класів використовуємо метод isinstance, приклад:

# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False
