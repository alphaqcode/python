﻿#函数式编程



#传入函数

def add(x,y,f):
    return f(x)+f(y)

add(-5,6,abs)


#map reduce
#利用maoreduce实现strToint
def fn(x,y):
    return x*10+y

def char2num(s):
    return {'0':0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

reduce(fn,map(char2num,'1985'))



##利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
##输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。


def uppercase(x):
    x = x[0].upper() + x[1:].lower
    return x

t = ['adam', 'LISA', 'barT']
map(uppercase,t)

#Python提供的sum()函数可以接受一个list并求和，
#请编写一个prod()函数，可以接受一个list并利用reduce()求积。
def prod(l):
    return reduce(lambda x,y:x*y,l)

t = range(1,6)
prod(t)


##过滤 fliter
def is_odd(n):
    return n%2 == 1

filter(is_odd,[1,2,3,4,5,6,7,8,9])


##sorted
def cmp_ignore_case(s1,s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0

sorted(['bob','about','Zoo','Credit','Alpha'],cmp_ignore_case)


##返回函数

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


f = lazy_sum(1,3,5,7,9)
f()

f1 = lazy_sum(1,3,5)
f2 = lazy_sum(1,3,5)
f1 == f2


##匿名函数
map(lambda x: x*x,[1,2,3,4,5,6])


##decorator  待搞懂



##偏函数





