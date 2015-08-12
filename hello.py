#!/usr/bin/env python
# -*- coding: utf-8 -*-
# hello.py

__author__ = 'AUROGON'

L = []
n = 1
while n < 99:
    L.append(n)
    n += 2
print(L)
print(len(L))
print(L[-1], L[-2])
print(L[2:5])
print(L[2:5:2])
print(L[::5])

# name = input('Please input your name:')
# print('Hello ', name)
print(u'中文字符串')
print('Hello %s, your score %% is %d' % ('maple', 90))
a = 1
if a is not None:
    print(a)


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(10))


def power(x, nn=2):
    s = 1
    while nn > 0:
        nn -= 1
        s *= x
    return s


print(power(5, 3))


def calc(*numbers):
    total = 0
    for b in numbers:
        total += b * b
    return total


print(calc(1, 2, 3, 4))
print(calc(*range(1, 6)))


def person(name, age, **kw):
    print('name: %s, age:%d, other:%s' % (name, age, kw))


person('tester', 22, city='GZ')
person('tester', 23, gender='M', job='Engineer')
person('tester', 24, **{'gender': 'M', 'job': 'Engineer'})


def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)


print(fac(100))


def fac2(n):
    return fac_iter(n, 1)


def fac_iter(n, p):
    if n == 1:
        return p
    return fac_iter(n - 1, n * p)


print(fac2(100))  # change to 200


def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[x] + L[x + 1] for x in range(len(L) - 1)] + [1]


n = 0
for t in triangles():
    print(t)
    n += 1
    if n == 10:
        break


def add(a, b, f):
    return f(a) + f(b)


print(add(-3, 9, abs))


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5])
l = list(r)
print(l)


def normalize(name):
    return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce


def prod(L):
    def mul(x, y):
        return x * y

    return reduce(mul, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


def str2float(s):
    def fn(x, y):
        return x * 10 + y

    def char2int(l):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[l]

    L = s.split('.')
    # print(reduce(lambda x, y: x / 10 + y, map(char2int, '7654')) / 10)
    # return reduce(fn, map(char2int, L[0])) + reduce(fn, map(char2int, L[1])) / power(10, len(L[1]))
    return reduce(lambda x, y: x * 10 + y, map(char2int, L[0])) + reduce(lambda x, y: x / 10 + y,
                                                                         map(char2int, L[1][::-1])) / 10

print('str2float(\'123.4567\') =', str2float('123.4567'))

def is_palindrome(n):
    return str(n) == str(n)[::-1]
# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0].lower()

def by_score(t):
    return t[1]

L2 = sorted(L, key=by_name)
L3 = sorted(L, key=by_score)
print(L2)
print(L3)

class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object(name: %s)' % self.name


print(Student('test'))

from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '==>', member, ',', member.value)
