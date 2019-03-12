Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruits=["banana","apple","avocado","melon","orange","mango"]
>>> for fruit in fruits:
	print(fruit)

	
banana
apple
avocado
melon
orange
mango
>>> numbers=[0,1,2,3,4,5,6,7,8,9]
>>> for number in numbers:
	print(number)

	
0
1
2
3
4
5
6
7
8
9
>>> fruits[0]
'banana'
>>> fruits[4]
'orange'
>>> fruits[0:4]
['banana', 'apple', 'avocado', 'melon']
>>> fruits[4:]
['orange', 'mango']
>>> fruits[-2:]
['orange', 'mango']
>>> a=[1,2,3]
>>> b=[4,5,6]
>>> c=a+b
>>> c
[1, 2, 3, 4, 5, 6]
>>> d=a*3
>>> d
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> fruits
['banana', 'apple', 'avocado', 'melon', 'orange', 'mango']
>>> fruits.apend("grapes")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    fruits.apend("grapes")
AttributeError: 'list' object has no attribute 'apend'
>>> fruits.append("grapes")
>>> fruits
['banana', 'apple', 'avocado', 'melon', 'orange', 'mango', 'grapes']
>>> fruits.add("peach")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    fruits.add("peach")
AttributeError: 'list' object has no attribute 'add'
>>> fruits.extend(["peach","kiwi"])
>>> fruits
['banana', 'apple', 'avocado', 'melon', 'orange', 'mango', 'grapes', 'peach', 'kiwi']
>>> fruits.remove("melon")
>>> fruits
['banana', 'apple', 'avocado', 'orange', 'mango', 'grapes', 'peach', 'kiwi']
>>> fruits.sort()
>>> fruits
['apple', 'avocado', 'banana', 'grapes', 'kiwi', 'mango', 'orange', 'peach']
>>> fruits.reverse()
>>> fruits
['peach', 'orange', 'mango', 'kiwi', 'grapes', 'banana', 'avocado', 'apple']
>>> fruits.pop()
'apple'
>>> fruits
['peach', 'orange', 'mango', 'kiwi', 'grapes', 'banana', 'avocado']
>>> del fruits[0]
>>> fruits
['orange', 'mango', 'kiwi', 'grapes', 'banana', 'avocado']
>>> fruits.replace("banana","dates")
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    fruits.replace("banana","dates")
AttributeError: 'list' object has no attribute 'replace'
>>> fruit[4]="dates"
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    fruit[4]="dates"
TypeError: 'str' object does not support item assignment
>>> numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> sum(numbers)
45
>>> sum(fruits)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    sum(fruits)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> min(numbers)
0
>>> max(numbers)
9
>>> fruits.append("banana")
>>> 
>>> fruits.append("mango")
>>> fruits
['orange', 'mango', 'kiwi', 'grapes', 'banana', 'avocado', 'banana', 'mango']
>>> fruits.count("banana")
2
>>> n=range(10)
>>> n
range(0, 10)
>>> for x in n:
	print(x)

	
0
1
2
3
4
5
6
7
8
9
>>> m=range(10,20)
>>> for x in m:
	print(x)

	
10
11
12
13
14
15
16
17
18
19
>>> for f in fruits:
	print(f)

	
orange
mango
kiwi
grapes
banana
avocado
banana
mango
>>> e=[x*10 for x in a]
>>> e
[10, 20, 30]
>>> f=[x*2 for x in e]
>>> f
[20, 40, 60]
>>> g=range(25,50)
>>> h=(x*x for x in g)
>>> h
<generator object <genexpr> at 0x030715F0>
>>> h=(x*x for x in g)
>>> h
<generator object <genexpr> at 0x030712B0>
>>> g=range(25,50)
>>> g
range(25, 50)
>>> h(x*x for x in g)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    h(x*x for x in g)
TypeError: 'generator' object is not callable
>>> h=(x*x for x in g)
>>> h
<generator object <genexpr> at 0x030715F0>
>>> h=[x*x for x in g]
>>> h
[625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401]
>>> h=[]
>>> for x in g"
SyntaxError: EOL while scanning string literal
>>> for x in g:
	h.append(x)

	
>>> 
>>> g
range(25, 50)
>>> for x in g:
	h.append(x)

	
>>> 
>>> 
>>> 
>>> h
[25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> y=x*x
>>> h[]
SyntaxError: invalid syntax
>>> h=[]
>>> y=x*x
>>> h.append(y)
>>> h
[2401]
>>> h[]
SyntaxError: invalid syntax
>>> h=[]
>>> for x in g:
	y=x*x
	h.append(y)

	
>>> h
[625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401]
>>> x
49
>>> x=[100,200,300,400,500]
>>> y[z//7 for z in x]
SyntaxError: invalid syntax
>>> y[z//7 for z in x]
SyntaxError: invalid syntax
>>> y=[z//7 for z in z]
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    y=[z//7 for z in z]
NameError: name 'z' is not defined
>>> y=[x//7 for x in x]
>>> y
[14, 28, 42, 57, 71]
>>> y=[]
>>> x=[100,200,300,400,500]
>>> y=[z%7 for x in x]
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    y=[z%7 for x in x]
  File "<pyshell#123>", line 1, in <listcomp>
    y=[z%7 for x in x]
NameError: name 'z' is not defined
>>> y=[x%7 for x in x]
>>> y
[2, 4, 6, 1, 3]
>>> y[]
SyntaxError: invalid syntax
>>> y=[]
>>> for x in x:
	x=x%7
	y.append(x)

	
>>> y
[2, 4, 6, 1, 3]
>>> y=[]
>>> for z in x:
	q=z%7
	y.append(x)

	
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    for z in x:
TypeError: 'int' object is not iterable
>>> y=[]
>>> for z in x:
	q=z%7
	y.append(q)

	
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    for z in x:
TypeError: 'int' object is not iterable
>>> x
3
>>> x=[100,200,300,400,500]
>>> for z in x:
	q=z%7
	y.append(q)

	
>>> y
[2, 4, 6, 1, 3]
>>> a=range(99,109)
>>> a
range(99, 109)
>>> b=[x*x for x in a]
>>> b
[9801, 10000, 10201, 10404, 10609, 10816, 11025, 11236, 11449, 11664]
>>> b=[]
>>> for x in a:
	d=x*x
	b.append(d)

	
>>> b
[9801, 10000, 10201, 10404, 10609, 10816, 11025, 11236, 11449, 11664]
>>> 
