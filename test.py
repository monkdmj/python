#!/usr/bin/env python3
# -*- coding: utf-8 -*-
age=7
if age>=18:
    print('zz')
    print('hh')
elif age>=6:
    print('kid')
else:
    print('baby')


#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
#x=0
#x=[]
x=''
if not x:
    print('赞')

s=int(input('birth:'))
if s>2000:
    print('00后')
#t=input('birth:')#3.0版本无raw_input
t=1000
if t>1990:
    print('90后')

age=20
if age>19:
    pass


def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x


def move(x,y,step,ang=0):
    #test.move(100,100,50) (150.0, 100.0)
    #test.move(100,100,50,3.14/6) (143.30790472027314, 124.98850513215513)
    import math
    nx=x+step*math.cos(ang)
    ny=y+step*math.sin(ang)
    return nx,ny

def enroll(name, gender, age=6, city='Beijing'):
    #enroll('Bob', 'M', 7)
    #enroll('Adam', 'M', city='Tianjin')
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

def add_end(L=[]):
    #add_end([1, 2, 3]) [1, 2, 3, 'END']
    #add_end() ['END'] add_end() ['END', 'END']ython函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
    #默认参数必须指向不变对象！
    
    L.append('END')
    return L

def add_end(L=None):
    #因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。
    if L is None:
        L = []
    L.append('END')
    return L

def calc(numbers):
    #calc([1,2,3]) 14
    #calc(1, 2, 3) 报错
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def calc2(*numbers):
    #calc2(1, 2, 3) 14
    #nums = [1, 2, 3] calc2(nums[0], nums[1], nums[2]) or calc2(*nums) -----14
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def person(name, age, **kw):
    #person('Michael', 30) name: Michael age: 30 other: {}
    #person('Adam', 45, gender='M', job='Engineer') name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
    #extra = {'city': 'Beijing', 'job': 'Engineer'} person('Jack', 24, **extra) name: Jack age: 24 other: {'job': 'Engineer', 'city': 'Beijing'}
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

