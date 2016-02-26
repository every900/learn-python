#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('hello,world')
print(100+200+300)
#print()会依次打印每个字符串，遇到逗号“,”会输出一个空格
print('The quick brown fox', 'jumps over', 'the lazy dog')
print('100 + 200 =', 100 + 200)
#name = input('pls input your name: ',)
#print('your name is',name)
#print('hello,',name)
print('1024*768','=',1024*768)
# print absolute value of an integer:
a = 100
if a >= 0:
    print(a)
else:
    print(-a)
print('整数\n Python可以处理任意大小的整数，当然包括负整数，在程序中的表示方法和数学上的写法一模一样，例如：1，100，-8080，0，等等。计算机由于使用二进制，所以，有时候用十六进制表示整数比较方便，十六进制用0x前缀和0-9，a-f表示，例如：0xff00，0xa5b4c3d2，等等。\n浮点数\n浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，比如，1.23x109和12.3x108是完全相等的。浮点数可以用数学写法，如1.23，3.14，-9.01，等等。但是对于很大或很小的浮点数，就必须用科学计数法表示，把10用e替代，1.23x109就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5，等等。整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差。')

print('\n字符串\n字符串是以单引号\'或双引号"括起来的任意文本，比如\'abc\'，"xyz\"等等。请注意，\'\'或""本身只是一种表示方式，不是字符串的一部分，因此，字符串\'abc\'只有a，b，c这3个字符。如果\'本身也是一个字符，那就可以用""括起来，比如\"I\'m OK\"包含的字符是I，\'，m，空格，O，K这6个字符。')
print('I\'m \"OK\"!')
print('转义字符\\可以转义很多字符，比如\\n表示换行，\\t表示制表符，字符\本身也要转义，所以\\\\表示的字符就是\\')
print('I\'m ok.')
print('I\'m learning\nPython.')
print('\\\n\\')
print('如果字符串里面有很多字符都需要转义，就需要加很多\\，为了简化，Python还允许用r\'\'表示\'\'内部的字符串默认不转义')
print('\\\t\\')
print(r'\\\t\\')
print('''line1
line2
line3''')
#print(r'''line1
#line2
#line3
#line4
#line5
#布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False，在Python中，可以直接用True、False表示布尔值（请注意大小写）
#布尔值可以用and、or和not运算
#and运算是与运算，只有所有都为True，and运算结果才是True
#or运算是或运算，只要其中有一个为True，or运算结果就是True
#not运算是非运算，它是一个单目运算符，把True变成False，False变成True
#	''')
#age = input('pls enter the age: ')
age = 20
if age >= 18:
    print('adult')
else:
    print('teenager')

print(r'''空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

此外，Python还提供了列表、字典等多种数据类型，还允许创建自定义数据类型，我们后面会继续讲到。''')

a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)
a = 'ABC'
b = a
a = 'XYZ'
print(b)
print(10/3)
print(9/3)
print(10//3)#地板除，只取整数
print(10%3)#余数运算，只取余数
print('无论整数做//除法还是取余数，结果永远是整数，所以，整数运算结果永远是精确的')
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print('n','=',123)
print('f','=',f)
print('n = ',n)
print('s1 =',s1)
print('')
print(r'\\')
print(r'\\')
print('"数据类型与变量"练习题：')
n=123
f=456.789
s1='Hello,world'
print('n=',n)
print('f=',f)
print('s1=',s1)
print('s2 = \'Hello, \\\'Adam\\\"')
print("s3= r'Hello,\"Bart\"'")
print("s4=r'''Hello,")
print("Lisa!'''")
print('"交作业"')

print('n = 123')
print('f = 456.789')
print('s1 = \'Hello, world\'')
print("s2 = \'Hello, \\'Adam\\''")
print("s3 = r\'Hello, \"Bart\"'")
print('s4 = r\'\'\'Hello, \n Lisa!\'\'\' ')

print('''n = 123
f = 456.789
s1 = 'Hello,world'
s2 = 'Hello, \\'Adam\\''
s3 = r'Hello, "Bart"'
s4 = r\'\'\'Hello,
Lisa!\'\'\'
''')

print('对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符')
print('ord(\'a\') =',ord('a'))
#print(ord('a'))
print('ord(\'中\') =',ord('中'))

print('chr(25991) =',chr(25991))
x = b'ABC'
print('x =',x)
print('要注意区分\'ABC\'和b\'ABC\'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。')
print('')
'ABC'.encode('ascii')
'中文'.encode('utf-8')

print('\'ABC\'encode ascii is: ','ABC'.encode('ascii'))
print('\'中文\'encode utf-8 is: ','中文'.encode('utf-8'))

b'ABC'.decode('ascii')
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

print('b\'ABC\' decode ascii is :',b'ABC'.decode('ascii'))
print('b\'\\xe4\\xb8\\xad\\xe6\\x96\\x87\'decode utf-8 is :',b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print()
print('要计算str包含多少个字符，可以用len()函数')
print(len('ABC'))
print(len('中文'))
print('\nlen()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数')
print( len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))
print('你可能猜到了，%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。')
print('\nHi, %s, you have $%d.' % ('Michael', 1000000))
print('常见的占位符：%d为整数，%f为浮点数，%s为字符串，%x为16进制整数')
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('Age: %s. Gender: %s' % (25, True))
print('有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%')
print('growth rate: %d %%' % 7)
s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print('rate is %.1f%%' % r)
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print('用索引来访问list中每一个位置的元素，记得索引是从0开始的')
print( classmates[0])
print( classmates[1])
print( classmates[0])
print( classmates[len(classmates) - 1])
print('如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素')
print(classmates[-1])
print(classmates[-2])
#追加list元素到末尾
print('list是一个可变的有序表，所以，可以往list中追加元素到末尾')
classmates.append('Adam')
print(classmates)
#插入list元素到指定位置
print('也可以把元素插入到指定的位置，比如索引号为1的位置')
classmates.insert(1, 'Jack')
print(classmates)
#删除list末尾元素
print('要删除list末尾的元素，用pop()方法')
classmates.pop()
print(classmates)
print('要删除指定位置的元素，用pop(i)方法，其中i是索引位置')
classmates.pop(1)
print(classmates)
#替换某个元素
print('要把某个元素替换成别的元素，可以直接赋值给对应的索引位置')
classmates[1]='Sarah'
print(classmates)
print('list里面的元素的数据类型也可以不同;list元素也可以是另一个list')
L = ['Apple', 123, True]
print(L)
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)
print(len(s))
print(s[2][1])
print('tuple和list非常类似，但是tuple一旦初始化就不能修改')
classmates = ('Michael', 'Bob', 'Tracy','hl')
print(classmates)
print(classmates[3])#取tuple中的数据也需要用【】
print('''不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来;
\nt=(1),定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。

所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义''')
t = (1,)
print(t)
t = ('a', 'b', ['A', 'B'])
print(t[2][0])
print(t[2][1])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
print(t[2][0])
print(t[2][1])
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
print('条件判断')
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

print('''根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。

也可以给if添加一个else语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了''')
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
print('if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else')
#if判断条件还可以简写,如下；只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
if x:
    print('True')
#birth = input('birth: ')
#if birth < 2000:
#    print('00前')
#else:
#    print('00后')
print('这是因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情')
#s = input('birth: ')
#birth = int(s)#转化字符串为整数
#if birth < 2000:
#    print('00前')
#else:
#    print('00后')
height = 1.75
weight = 80.5
bmi =weight/height/height
print(bmi)
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')
print('\n循环\n')
print('''Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来;
for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句''')
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)
print('如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数')
print(list(range(5)))
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
print('\n第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现')
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello,%s!'% name)

print('''dict
    dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度''')
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print( d['Michael'])
print('把数据放入dict的方法，除了初始化时指定外，还可以通过key放入')
d['Adam'] = 67
print(d['Adam'])
print(d)
print('''要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
    二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value''')
print('Thomas' in d)
print(d.get('Thomas'))
print(d.get('Thomas', -1))
print('要删除一个key，用pop(key)方法，对应的value也会从dict中删除')
print(d.pop('Bob'))
print(d)
print('''\n和list比较，dict有以下几个特点：

查找和插入的速度极快，不会随着key的增加而增加；
需要占用大量的内存，内存浪费多。
而list相反：

查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。
dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：''')

print('''set

set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

要创建一个set，需要提供一个list作为输入集合''')
s = set([1,2,3])
print(s)
s = set([1, 1, 2, 2, 3, 3])
print(s)#重复元素在set中自动被过滤
print('通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果')
s.add(4)
print(s)
s.add(4)
print(s)
print('通过remove(key)方法可以删除元素')
s.remove(4)
print(s)
print('set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作')
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)#交集
print(s1|s2)#并集
s3 = [1,2,3]
s = set(s3)
print(s)
a = ['c', 'b', 'a']
a.sort()
print(a)
a = 'abc'
print(a.replace('a', 'A'))
print(a)
print('\n函数\n')
def __sum__(n):
    return(n*n+1)

s = 0
for n in range(101):
    s = __sum__(n) + s
    print('__sum__(', n, ') =',  __sum__(n), '   s =', s)
print(s)
print(abs(100))#绝对值函数
print(abs(-100))
print(abs(10.02))
max(1,2,3)
print(max(1,2,3))#max函数max()可以接收任意多个参数，并返回最大的那个
print(max(2, 3, 1, -5))
print('数据类型转换')
print(int('123'))
print(int(12.34))
print( float('12.34'))
print(str(1.23))
print(bool(1))
print(bool(''))
print('函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”')
a = abs # 变量a指向abs函数
print(a(-1)) # 所以也可以通过a调用abs函数
#n1 = int(input('请输入一个整数：'))
#print(hex(n1))
#n1 = input('请输入一个整数：')
#print(hex(n1))
#n2 = int(input('请输入另一个整数：'))
#print(hex(n2))
print('\n定义函数')
print('在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回')
#def my_abs(x):
#    if x >= 0:
#        return x
#    else:
#        return -x
#print(my_abs(-102))
#from abstest import my_abs
#print(my_abs(-102))
#print(my_abs(-1))
print('''空函数
    如果想定义一个什么事也不做的空函数，可以用pass语句''')
def nop():
    pass
print('pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来')
if age >= 18:
    pass
print('''参数检查
数据类型检查可以用内置函数isinstance()实现''')
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-102))
#print(my_abs('A'))
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
r = move(100, 100, 60, math.pi / 6)
print(r)
print('原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便')
print(math.sqrt(2))
def quadratic(a, b, c):
    if not isinstance (a,(int,float)):
        raise TypeError('不能含有字母,请重新输入3个实数')
    if not isinstance (b,(int,float)):
        raise TypeError('不能含有字母,请重新输入3个实数')
    if not isinstance (c,(int,float)):
        raise TypeError('不能含有字母,请重新输入3个实数')

    if a==0:
        x=-c/b
        return x
    elif (b*b)<(4*a*c):
        raise TypeError('方程无解 ')
    else:
        x1=((-b + math.sqrt(b*b-4*a*c))/(2*a))
        x2=((-b - math.sqrt(b*b-4*a*c))/(2*a))
        if x1==x2:
            return x1
        else:
            return x1,x2

#print(quadratic(1,2,3))
#print(quadratic(a,2,3))
print(quadratic(1,5,3))
print(quadratic(0,2,3))
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5, 3))
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5))
print('''默认参数可以简化函数的调用。设置默认参数时，有几点要注意：

一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

二是如何设置默认参数。

当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。''')
print(power(5,5))
def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)
print(enroll('Sarah', 'F'))

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

print(enroll('Sarah', 'F'))
print(enroll('Bob', 'M', 7))
print(enroll('Adam', 'M', city='Tianjin'))

def add_end(L=[]):
    L.append('END')
    return L
print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))
print(add_end())
print(add_end())
print('定义默认参数要牢记一点：默认参数必须指向不变对象！')

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end())
print(add_end())
print('\n可变参数')
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc([1, 2, 3]))
print(calc((1, 3, 5, 7)))

def calc(*numbers):#简化
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 2, 3))
print(calc(1,3,5,7))
print('定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数')
print(calc(1, 2))
print(calc())
print('python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去')
nums = [1, 2, 3]
print(calc(*nums))

print('关键字参数')
print('可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict')
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
print(person('Michael', 30))
print(person('Bob', 35, city='Beijing'))
print(person('Adam', 45, gender='M', job='Engineer'))
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, city=extra['city'], job=extra['job']))
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, **extra))#简化写法
print('**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra')

print('\n命名关键字参数')
print('对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。\n仍以person()函数为例，我们希望检查是否有city和job参数.')
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

print(person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456))
print('和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数')
def person(name, age, *, city, job):
    print(name, age, city, job)

print( person('Jack', 24, city='Beijing', job='Engineer'))

def person(name, age, *, city='Beijing', job):#默认值
    print(name, age, city, job)
print(person('Jack', 24, job='Engineer'))
print('使用命名关键字参数时，要特别注意，*不是参数，而是特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数')

def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass

print('\n参数组合\n在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用，除了可变参数无法和命名关键字参数混合。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。')
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

print(f1(1, 2))
print( f1(1, 2, c=3))
print(f1(1, 2, 3, 'a', 'b'))
print(f1(1, 2, 3, 'a', 'b', x=99))
print(f2(1, 2, d=99, ext=None))
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
print(f1(*args, **kw))
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
print( f2(*args, **kw))
print('''Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数不要忘了写分隔符*，否则定义的将是位置参数。''')

print('\n递归函数')
print('在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。')
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(1))
print(fact(5))
print(fact(10))
print('使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)')
#print(fact(1000))
print('''解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：''')
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
#可以看到，return fact_iter(num - 1, num * product)仅返回递归函数本身，num - 1和num * product在函数调用前就会被计算，不影响函数调用。
print(fact(997))
#栈溢出此处最大值为997
print('''尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。

遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。

小结：
使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。

Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。''')
def hanoi(n,x,y,z):
    if n==1:
        print(x,'-->',z)
    else:
        hanoi(n-1,x,z,y)#将前n-1个盘子从x移动到y上
        hanoi(1,x,y,z)#将最底下的最后一个盘子从x移动到z上
        hanoi(n-1,y,x,z)#将y上的n-1个盘子移动到z上
#n=int(input('请输入汉诺塔的层数：'))
#hanoi(n,'x','y','z')
print('\n神奇的汉诺塔：在世界中心贝拿勒斯（在印度北部）的圣庙里，一块黄铜板上插着三根宝石针。印度教的主神梵天在创造世界的时候，在其中一根针上从下到上地穿好了由大到小的64片金片，这就是所谓的汉诺塔。不论白天黑夜，总有一个僧侣在按照下面的法则移动这些金片：一次只移动一片，不管在哪根针上，小片必须在大片上面。僧侣们预言，当所有的金片都从梵天穿好的那根针上移到另外一根针上时，世界就将在一声霹雳中消灭，而梵塔、庙宇和众生也都将同归于尽.\n实际计算结果是当n=64时，时间将会是5845.54亿年以上')

print('\n\n高级特性')

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2

print(L)
print('''\n但是在Python中，代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好。

基于这一思想，我们来介绍Python中非常有用的高级特性，1行代码能实现的功能，决不写5行代码。请始终牢记，代码越少，开发效率越高。
;
切片''')
print('取一个list或tuple的部分元素是非常常见的操作')
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print([L[0], L[1], L[2]])#笨办法，直接查
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)#循环办法
print('对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作')
print(L[0:3])
print('''L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。

如果第一个索引是0，还可以省略：''')
print(L[:3])
print(L[1:3])
print( L[-2:])
print(L[-2:-1])
L = list(range(100))
print(L)
print(L[:10])#前10个数
print(L[-10:])#后10个数
print( L[10:20])#前11-20个数
print( L[:10:2])#前10个数，每两个取一个
print( L[::5])#所有数，每5个取一个
#甚至什么都不写，只写[:]就可以原样复制一个list
print('''tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple.
    字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串''')
print((0, 1, 2, 3, 4, 5)[:3])
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])
print('''\n迭代
    如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
    在Python中，迭代是通过for ... in来完成的，而很多语言比如C或者Java，迭代list是通过下标完成的''')
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
print('默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。')
for ch in 'ABC':
    print(ch)
from collections import Iterable
isinstance('abc', Iterable)# str是否可迭代
print(isinstance('abc', Iterable))
isinstance([1,2,3], Iterable) # list是否可迭代
print(isinstance([1,2,3], Iterable)) # list是否可迭代
isinstance(123, Iterable) # 整数是否可迭代
print( isinstance(123, Iterable))
#如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
print('''\n列表生成式\n
    列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。''')
list(range(1, 11))
print(list(range(1, 11)))
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)
[x * x for x in range(1, 11)]
print([x * x for x in range(1, 11)])
print('''写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。

for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方''')
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])
print([m + n for m in '123' for n in '456'])
#运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os # 导入os模块，模块的概念后面讲到
print( [d for d in os.listdir('.')] )# os.listdir可以列出文件和目录
#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)
#列表生成式也可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

#最后把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
L1 = ['Hello', 'World', 18, 'Apple', None]
#print([s.lower() for s in L])
L2 = []
for s in L1:
    if isinstance(s,str):
        L2.append(s.lower())
    else:
        pass
print(L2)
L2 = [x.lower() for x in L1 if isinstance(x,str)]
print(L2)

print('\n 生成器')
print('''通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator''')
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)
#创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator
print(next(g))
print(next(g))
print(next(g))
print(next(g))
#generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。

#当然，上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象：
g = (x * x for x in range(10))
for n in g:
    print(n)
print('''所以，我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误。

generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。

比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
1, 1, 2, 3, 5, 8, 13, 21, 34, ...''')
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
print( fib(6))

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
f = fib(6)
print(f)
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o = odd()
print(next(o))
print(next(o))
print(next(o))
#print(next(o))
for n in fib(6):
    print(n)
#用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g = fib(6)
while True:
    try:
         x = next(g)
         print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
print('''generator是非常强大的工具，在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。

要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。

请注意区分普通函数和generator函数，普通函数调用直接返回结果：
>>> r = abs(6)
>>> r
6
generator函数的“调用”实际返回一个generator对象：

>>> g = fib(6)
>>> g
<generator object fib at 0x1022ef948>
\n杨辉三角--没搞懂下述算法''')
def triangles():
    L1=[1]
    while True:
        yield L1
        L1.append(0)
        L2=[x for x in L1]
        i=0
        while i<len(L2):
            L1[i]=L2[i]+L2[i-1]
            i=i+1
    return 'done'
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

def triangles():#NB的简洁程序，没懂。
    b = [1]
    while True:
        yield b
        b = [1] + [b[i] + b[i+1] for i in range(len(b)-1)] + [1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

print('''\n   迭代器
    \n我们已经知道，可以直接作用于for循环的数据类型有以下几种：

一类是集合数据类型，如list、tuple、dict、set、str等；

一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

可以使用isinstance()判断一个对象是否是Iterable对象：''')
from collections import Iterable
isinstance([], Iterable)
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(123, Iterable))

print('''而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。

可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

可以使用isinstance()判断一个对象是否是Iterator对象：''')

from collections import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print(range(10))
print('''生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

把list、dict、str等Iterable变成Iterator可以使用iter()函数：''')
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))
print('''你可能会问，为什么list、dict、str等数据类型不是Iterator？

这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

小结

凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

Python的for循环本质上就是通过不断调用next()函数实现的''')
for x in [1, 2, 3, 4, 5]:
    pass
#实际上完全等价于：
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

print('\n函数式编程')
print('''函数是Python内建支持的一种封装，我们通过把大段代码拆成函数，通过一层一层的函数调用，就可以把复杂任务分解成简单的任务，这种分解可以称之为面向过程的程序设计。函数就是面向过程的程序设计的基本单元。

而函数式编程（请注意多了一个“式”字）——Functional Programming，虽然也可以归结到面向过程的程序设计，但其思想更接近数学计算。

我们首先要搞明白计算机（Computer）和计算（Compute）的概念。

在计算机的层次上，CPU执行的是加减乘除的指令代码，以及各种条件判断和跳转指令，所以，汇编语言是最贴近计算机的语言。

而计算则指数学意义上的计算，越是抽象的计算，离计算机硬件越远。

对应到编程语言，就是越低级的语言，越贴近计算机，抽象程度低，执行效率高，比如C语言；越高级的语言，越贴近计算，抽象程度高，执行效率低，比如Lisp语言。

函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。

高阶函数 Higher-order function
变量可以指向函数''')
abs(-10)
abs
print(abs(-10))
print(abs)
x = abs(-10)
print(x)
f = abs
print(f)
print('结论：函数本身也可以赋值给变量，即：变量可以指向函数')
f = abs
print(f(-10))
print('函数名也是变量')
print('那么函数名是什么呢？函数名其实就是指向函数的变量！对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！')
print('''如果把abs指向其他对象，会有什么情况发生？

>>> abs = 10
>>> abs(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
把abs指向10后，就无法通过abs(-10)调用该函数了！因为abs这个变量已经不指向求绝对值函数而是指向一个整数10！

当然实际代码绝对不能这么写，这里是为了说明函数名也是变量。要恢复abs函数，请重启Python交互环境。

注：由于abs函数实际上是定义在__builtin__模块中的，所以要让修改abs变量的指向在其它模块也生效，要用__builtin__.abs = 10。''')
#abs = 10
print(abs)
print('传入函数')
print('既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数')
def add(x, y, f):
    return f(x) + f(y)
print('''当我们调用add(-5, 6, abs)时，参数x，y和f分别接收-5，6和abs，根据函数定义，我们可以推导计算过程为：

x = -5
y = 6
f = abs
f(x) + f(y) ==> abs(-5) + abs(6) ==> 11
return 11''')
#add(-5, 6, abs)
print(add(-5, 6, abs))
print('把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式')

print('''map/reduce
    如果你读过Google的那篇大名鼎鼎的论文“MapReduce: Simplified Data Processing on Large Clusters”，你就能大概明白map/reduce的概念。

我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：

map''')
def f(x):
    return x*x
print
r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))
print('''map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

你可能会想，不需要map()函数，写一个循环，也可以计算出结果''')
L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)
print('map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串')
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
#print 'hello world'
print('reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算')
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x, y):
    return x + y
print(reduce(add, [1, 3, 5, 7, 9]))
from functools import reduce
def fn(x, y):
    return x * 10 + y
print(reduce(fn,[1,3,5,7,9]))
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print(reduce(fn, map(char2num, '13579')))
from functools import reduce
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

from functools import reduce
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

def  str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))

print(str2int('13579'))

print('利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字')
def normalize(name):
    return name[:1].upper()+name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

print('Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积')
def prod(L):
    return reduce((lambda x,y:x*y),L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

print('利用map和reduce编写一个str2float函数，把字符串\'123.456\'转换成浮点数123.456')
#没搞懂
def str2float(s):
    l = s.split('.')
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, l[0]))+reduce(fn, map(char2num, l[1]))/pow(10,len(l[1]))

print('str2float(\'123.456\') =', str2float('123.456'))

print('\nfilter过滤器')
print('''Python内建的filter()函数用于过滤序列。

和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。''')
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd,[1,2,4,5,6,9,10,15])))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['A','','B',None,'C','d',''])))
print('''可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。

注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

用filter求素数

计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：

首先，列出从2开始的所有自然数，构造一个序列：

2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：

3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：

5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数5，然后用5把序列的5的倍数筛掉：

7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

不断筛下去，就可以得到所有的素数。''')

def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n
def _not_divisible(n):
    return lambda x:x % n > 0
def primes():
    yield 2
    it = _odd_iter()#初始序列
    while True:
        n = next(it)#返回序列的第一个数
        yield n
        it = filter(_not_divisible(n),it)#构造新序列

#这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。
#由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
#打印1000以内的素数
for n in primes():
    if  n < 10:
        print(n)
    else:
        break
#注意到Iterator是惰性计算的序列，所以我们可以用Python表示“全体自然数”，“全体素数”这样的序列，而代码非常简洁。

def is_palindrome(n):
    return str(n) == str(n)[::-1]

#测试：
output = filter(is_palindrome, range(1, 1000))
print(list(output))
print('\nfilter()的作用是从一个序列中筛出符合条件的元素。由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。')
print('''\nsorted
    排序算法

排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。''')
print(sorted([36, 5, -12, 9, -21]))
#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
print(sorted([36,5,-12,9,-21],key=abs))
print('''key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。对比原始的list和经过key=abs处理过的list：

list = [36, 5, -12, 9, -21]

keys = [36, 5,  12, 9,  21]
然后sorted()函数按照keys进行排序，并按照对应关系返回list相应的元素：

keys排序结果 => [5, 9,  12,  21, 36]
                |  |    |    |   |
最终结果     => [5, 9, -12, -21, 36]''')
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print('''默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。

现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，只要我们能用一个key函数把字符串映射为忽略大小写排序即可。忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。

这样，我们给sorted传入key函数，即可实现忽略大小写的排序：''')
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.upper))
#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.upper,reverse=True))
#高阶函数的抽象能力是非常强大的，而且，核心代码可以保持得非常简洁。
#sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]

L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
    return t[1]
L2 = sorted(L,key=by_score,reverse=True)
print(L2)
print('''\n返回函数
    函数作为返回值

高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。''')
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())
print('''在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力
    请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：''')
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1==f2)
print('f1()和f2()的调用结果互不影响。')
print(f1())
print(f2())
print('''\n闭包

注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。

另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。''')

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

#在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。

#你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：
print(f1())
print(f2())
print(f3())
print('''全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变''')

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
#缺点是代码较长，可利用lambda函数缩短代码。
print('''小结

一个函数可以返回一个计算结果，也可以返回一个函数。

返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。''')
















































































