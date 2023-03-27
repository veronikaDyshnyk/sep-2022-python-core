# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
from typing import Callable


def notebook() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list[str]:
        nonlocal todo_list
        return todo_list

    return add_todo, get_all


add, get = notebook()

add('wake up')
add('work')
add('die')
l = get()
print(l)


# 2)протипізувати перше завдання

# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#

# def expanded_form(number: int) -> str:
#     st = str(number)
#     # return ' + '.join(ch + '0' * (len(st) - i - 1) for i, ch in enumerate(st) if ch != '0')
#     return ' + '.join(ch + '0' * (len(st) - i - 1) for i, ch in enumerate(st) if ch != '0') + f' = {st}'
#
#
# print(expanded_form(1010))


# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'


# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функцій

def count_decor(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        res = func(*args, **kwargs)
        print(f'{count=}')
        print('*' * 20)
        return res

    return inner


@count_decor
def expanded_form(number: int) -> str:
    st = str(number)
    print(st)
    # return ' + '.join(ch + '0' * (len(st) - i - 1) for i, ch in enumerate(st) if ch != '0')
    return ' + '.join(ch + '0' * (len(st) - i - 1) for i, ch in enumerate(st) if ch != '0') + f' = {st}'


print(expanded_form(2020))
print(expanded_form(10938))
print(expanded_form(1))
print(expanded_form(22))
