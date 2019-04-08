# -*- coding: utf-8 -*-


__author__ = 'WangJianyu'
__date__ = '2019/2/15'

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_number = record
print(name)
print(email)
print(phone_number)

records = [('foo', 1, 2),
           ('bar', 'hello'),
           ('foo', 3, 4), ]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'

uname, *fields, homedir, sh = line.split(':')
print(uname)
print(fields)
print(homedir)
print(sh)

record = ('ACME', 50, 123.45, (12, 18, 2012))

name, *_ = record
print(name)
print(*_)

items = [1, 10, 7, 4, 5, 9]

head, *tail = items
print(head)
print(tail)


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


print(sum(items))

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record

print(name)
print(*_)
print((*_, year))

items = [1, 10, 7, 4, 5, 9]
items2 = [1]


def sum(items):
    head, *tail = items

    return head + sum(tail) if tail else head


print(sum(items))

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    print(previous_lines)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)


q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.appendleft(4)
print(q)
q.popleft()
print(q)
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

li = [11, 22, 33]
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1}, {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(cheap)
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.heapify(nums)
print(nums)
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

print(d)

from collections import OrderedDict


def ordered_dict():
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    for key in d:
        print(key, d[key])
    import json
    print(json.dumps(d))


ordered_dict()

prices = {'ACME': 45.23,
          'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75
          }

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
sorted_price = sorted(zip(prices.values(), prices.keys()))
print(min_price)
print(max_price)
print(sorted_price)

min_value = prices[min(prices, key=lambda k: prices[k])]
print(min_value)

a = {
    'x': 1,
    'y': 2,
    'z': 3}
b = {
    'w': 10,
    'x': 11,
    'y': 2}
# 找到共同的关键
print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())

c = {key: a[key] for key in a.keys() - {'z', 'w'}}

print(c)
for key in a.keys() - {'z', 'w'}:
    print({key: a[key]})

for key in b.keys() - {'z', 'w'}:
    print({key: b[key]})

a = [1, 5, 2, 1, 9, 1, 5, 10]


# def dedupe(items):
#     seen = set()
#     for item in items:
#         if item not in seen:
#             yield item
#             seen.add(item)
#
# for i in dedupe(a):
#     print(i)

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
    'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under'
]

words_counts = Counter(words)
# 出现频率最高的三个单词
print(type(words_counts))
top_three = words_counts.most_common(3)
print(top_three)

print(words_counts['not'])
print(words_counts['eyes'])
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    words_counts[word] += 1
print(words_counts['eyes'])

words_counts.update(morewords)

aa = Counter(words)
bb = Counter(morewords)
print(aa)
print(bb)
print(aa + bb)
print(aa - bb)
print(bb - aa)

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}, {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}, {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_uid)
print((rows_by_fname))

rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfanme = sorted(rows, key=lambda r: (r['lname'], r['fname']))

print(min(rows, key=itemgetter('uid')))
print(max(rows, key=itemgetter('uid')))


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))


sort_notcompare()
users = [User(23), User(3), User(99)]
from operator import attrgetter

print(sorted(users, key=attrgetter('user_id')))

print(min(users, key=attrgetter('user_id')))
print(max(users, key=attrgetter('user_id')))

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'}, {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'}, {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}, {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'}, {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
from operator import itemgetter
from itertools import groupby

# rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    # print(date)
    for i in items:
        print(i)

from collections import defaultdict

rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
print(rows_by_date)

for r in rows_by_date['07/01/2012']:
    print(r)

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])

pos = (n for n in mylist if n > 0)

for i in pos:
    print(i)

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

import math

print([math.sqrt(n) for n in mylist if n > 0])

prices = {'ACME': 45.23,
          'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75
          }
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)

tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)
p3 = {key: prices[key] for key in prices.keys() & tech_names}
print(p3)

from collections import namedtuple

Subscriber = namedtuple('Subsriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)
print(len(sub))


#
# class Node:
#     def __init__(self, value):
#         self._value = value
#         self._children = []
#
#     def __repr__(self):
#         return 'Node({!r})'.format(self._value)
#
#     def __iter__(self):
#         return iter(self._children)
#
#     def add_child(self,node):
#         self._children.append(node)
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 4, 0.5):
    print(n)

print(list(frange(0, 4, 0.5)))


# if __name__ == '__main__':
#     root = Node(0)
#     child1 = Node(1)
#     child2 = Node(2)
#     root.add_child(child1)
#     root.add_child(child2)

#     for ch in root:#
#         print(ch)


class Node:

    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


class Pair:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair(%r,%r)' % (self.x, self.y)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


p = Pair(3, 4)
print(p.__repr__())
print(p)

_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}', 'mdy': '{d.month}/{d.day}/{d.year}', 'dmy': '{d.day}/{d.month}/{d.year}'}


class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'

        fmt = _formats[code]
        return fmt.format(d=self)


d = Date(2012, 12, 21)

print(format(d, ))

from datetime import date

d = date(2012, 12, 21)

print(format(d))

print(format(d, '%y, %m, %d, %h, %m, %s, %w, %j, %d'))


class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


a = Person('Guido')
print(a.first_name)

import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, str(end - start) + ' second')
        return result

    return wrapper


@timethis
def countdown(n):
    while n > 0:
        n -= 1


print(countdown(19999))


class A:
    @classmethod
    def method(cls):
        pass

    method = classmethod(method)


import logging


def logged(level, name=None, message=Node):

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        return wrapper

    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

print(add(1,1))
print(spam())

from functools import  wraps

class Aa:
    def decorator1(self,func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)
        return wrapper

    @classmethod
    def decorator2(cls,func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper

a = Aa()

@a.decorator1
def spam():
    pass

@Aa.decorator2
def grok():
    pass

class Person:
    first_name = property()

    @first_name.getter
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self,value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value












