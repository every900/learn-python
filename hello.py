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


















































