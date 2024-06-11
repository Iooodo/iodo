# def - объявление функции (глагол, прилагательное)
# ctrl + клик


# lambda - анонимная функция

# # # # # start = 2
# # # # # stop = 44
# # # # # step = 3
# # # # # line_count = 4
# # # # # for i in range(start, stop + 1, step * line_count):
# # # # #     for j in range(i, i + step * line_count - 1, step):
# # # # #         if j <= stop:
# # # # #             print(j, end=" ")
#         else:
#             break
# .print().
# # # #     print("FOO")
# # # #     print("FOO")
# # # #     print("FOO")
# # # #     return "HELLO", "WORLD"
# # # #
# # # #
# # # # def bar(a, b=None, *args, c=6, **kwargs):
# # # #     print(a)
# # # #     print(b)
# # # #     print(c)
# # # #     print(args)
# # # #     print(kwargs)
# # # #
# # # #
# # # # def baz(e, *, a, b, c, d):
# # # #     print(a)
# # # #     print(b)
# # # #     print(c)
# # # #     print(d)
# # # #     print(e)
# # # #
# # # #
# # # # def fu(a, b, c, d, e):
# # # #     print(a, b, c, d, e)
# # # #
# # # #
# # # # def func(a):
# # # #     a["key"] = "value"
# # # #
# # # #
# # # # # data = {}
# # # # # func(data)
# # # # # print(data)
# # # #
# # # #
# # # # def ll(b, a=None):
# # # #     if a is None:
# # # #         a = []
# # # #     a.append(b)
# # # #     print(a)
# # # #
# # #
# # #
# # # a = 5
# # #
# # #
# # # def foo():
# # #     a = 4
# # #
# # #     def bar():
# # #         nonlocal a
# # #         print(a)
# # #
# # #     bar()
# # #
# # #
# # # # f = globals().get("foo")
# # # # f()
# # #
# # #
# # # # callback
# # # def wrapper(func):
# # #     func()
# # #
# # #
# # # def decorator():
# # #     def wrapped():
# # #         print("wrapped")
# # #
# # #     return wrapped
# #
# #
# # # anonim = lambda x, y: (x * y) ** 2
# #
# #
# # # objs = [3, 4, "-2", -54, 2, 5, "45", "-234"]
# # # # [3, 4, 2, 54, 2, 5, 45, 234]
# # # print(min(objs, key=lambda x: abs(int(x))))
# # # print(objs)
# #
# #
# # def geom_range(start, step, count):
# #     while count:
# #         count -= 1
# #         yield start
# #         start *= step
# #
# #
# # numbers = [1, 2, 3, (1, 2, 3, {1, 2, 3}, 4, 5, 6), 4, 5, 6]
# #
# #
# # def recursive_multiply(numbers):
# #     s = 1
# #     for number in numbers:
# #         if isinstance(number, (int, float)):
# #             s *= number
# #         elif isinstance(number, (list, tuple, set)):
# #             s *= recursive_multiply(number)
# #     return s
#
#
# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"была вызвана функция {func.__name__}")
#         print(f"{args=}")
#         print(f"{kwargs=}")
#         result = func(*args, **kwargs)
#         print(f"{result=}")
#         return result
#
#     return wrapper
#
#
# def decorator(a):
#     def wrapper(func):
#         def wrapped(*args):
#             numbers = [number * a for number in args]
#             return func(*numbers)
#
#         return wrapped
#     return wrapper
#
#
# # @decorator(2)
# # @log
# # def multiply(*args):
# #     m = 1
# #     for i in args:
# #         m *= i
# #     return m
# #
# #
# # print(multiply(1, 2, 3))
#
#
# def bread(func):
#     def wrapped():
#         print("/-------\\")
#         func()
#         print("\\_______/")
#
#     return wrapped
#
#
# def onion(func):
#     def wrapped():
#         print("=========")
#         func()
#         print("=========")
#
#     return wrapped
#
#
# @bread
# @onion
# def beef():
#     print("*********")
#
#
# def foo(x, y):
#     return x ** y
#
#
# numbers = [2, 4, 6, 8, 10]
# result = map(foo, numbers, numbers)
#
#
# # words = ["Hello", "age", "apple", "belhard", "aa"]
# # res = filter(lambda x: len(x) < 5, words)
# # from itertools import zip_longest
# # from functools import reduce
#
# # text = "Hell"
# # numbers = [1, 2, 3, 4, 5]
# # objs = (True, False, None)
# # z = zip_longest(text, numbers, objs, fillvalue="НЕТУ")
# # for i in z:
# #     print(i)
#
# # numbers = [2, 4, 6, 8]
# # result = reduce(lambda x, y: x * y, numbers)
# # print(result)
# from typing import Union, Dict
#
# def foo(a: list[dict]) -> int:
#     return "rdftgyhujiko"
#
#
# data: Dict[str, Union[str, int]] = {}

#
# def foo(a: list, *args: str, **kwargs: list) -> None:
#     for i in a:  # type: int
#         pass

# def simple_func(name):
#     return f'Hello {name}!'
# result = simple_func('vasya')
# print(result)

# def simple_func(n):
#     def nested_func():
#         print('i am funk')
#     for i in range(n):
#         nested_func()
# simple_func(4)

# def multiply(x):
#     def power(y):
#         return x * y
#     return power
#
# x_3 = multiply(4)
# print(x_3(6))
#
# simple_func = lambda x, n: x**n
# print(simple_func(2, 2))

# numbers = ['1', '3', '4']
# numbers = list(map(float, numbers))
# print(numbers)

# text = ['s', 't', '4', '77', 'd']
# text = list(filter(lambda x: x.isdigit(), text))
# print(text)

# a = [3, 4, 6, 5]
# b = 'podke'
# c = (None, True, False)
# res = list(zip(a, b, c))
# print(res)

# def simple_func(a, b = None):
#     print(a, b)
# simple_func(4, b = 5)

# def simple_func(*args):
#     print(args)
# simple_func(4, 5, 6, 3, 'p')

# def simple_func(**kwargs):
#     print(kwargs)
# simple_func(a=4, b=5, c=6, d=3, e='p')

# def simple_func(n):
#     for i in range(n):
#         yield i
# a = simple_func(4)
# print('kow')
# print(next(a))
# print('kow')
# print(next(a))
# print('kow')
# print(next(a))

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print('ihjdj')
#         result = func(*args, **kwargs)
#         print('after')
#         return result
#     return wrapper
#
# @decorator
# def hello(name):
#     print(f"Hello, {name}")
#
# hello('Kate')

# import time
#
# def delay(seconds=1):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print('before')
#             time.sleep(seconds)
#             result = func(*args, **kwargs)
#             print('after')
#             return result
#         return wrapper
#     return decorator
#
# @delay(4)
# def hello(name):
#     print (f'Hello, {name}')
# hello("Kat")

def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n*factorial_recursive(n-1)
print(factorial_recursive(4))