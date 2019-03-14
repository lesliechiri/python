Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=(1,2,3,4)
>>> b=("a","b","c","d")
>>> a.append(5)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a.append(5)
AttributeError: 'tuple' object has no attribute 'append'
>>> b.remove("c")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    b.remove("c")
AttributeError: 'tuple' object has no attribute 'remove'
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a.pop()
AttributeError: 'tuple' object has no attribute 'pop'
>>> b.pop()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    b.pop()
AttributeError: 'tuple' object has no attribute 'pop'
>>> a.reverse()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.reverse()
AttributeError: 'tuple' object has no attribute 'reverse'
>>> b.sort()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    b.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> a=(1,2,3,4)
>>> b=("a","b","c","d")
>>> for x in a:
	print(x)

	
1
2
3
4
>>> c=list(a)
>>> c
[1, 2, 3, 4]
>>> d=[x for x in a]
>>> d
[1, 2, 3, 4]
>>> a
(1, 2, 3, 4)
>>> f=a+b
>>> f
(1, 2, 3, 4, 'a', 'b', 'c', 'd')
>>> a*3
(1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
>>> a
(1, 2, 3, 4)
>>> "b" in b
True
>>> "e" in b
False
>>> 5 in a
False
>>> 1 in a
True
>>> y=(a)
>>> y
(1, 2, 3, 4)
>>> y=[a]
>>> y
[(1, 2, 3, 4)]
>>> y=(x)
>>> y
4
>>> y=(x for x in a)
>>> y
<generator object <genexpr> at 0x0391D8F0>
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a=[1,2,3,4,5,3,7]
>>> b=set(a)
>>> b
{1, 2, 3, 4, 5, 7}
>>> c={"a","b","c","a","c","c"}
>>> c
{'a', 'b', 'c'}
>>> c
{'a', 'b', 'c'}
>>> d={"a","A","b","B"}
>>> d
{'a', 'B', 'b', 'A'}
>>> d={"a","A","b","B","a","b","A"}
>>> D
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    D
NameError: name 'D' is not defined
>>> d
{'a', 'B', 'b', 'A'}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> s1={1,2,3,,4}
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> s1={1,2,3,4}
>>> s2={3,4,5,6}
>>> s2.add(7)
>>> s2
{3, 4, 5, 6, 7}
>>> s2.remove(7)
>>> s2
{3, 4, 5, 6}
>>> s1.discard(4)
>>> s1
{1, 2, 3}
>>> s2.remove(7)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    s2.remove(7)
KeyError: 7
>>> s1.discard(4)
>>> s1
{1, 2, 3}
>>> s1.difference(s2)
{1, 2}
>>> s2.difference(s1)
{4, 5, 6}
>>> s1.intersection(s2)
{3}
>>> 
>>> s2.intersection(s1)
{3}
>>> s2.union(s1)
{1, 2, 3, 4, 5, 6}
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6}
>>> 
>>> 
>>> 
>>> 
>>> s1.extend(s2)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    s1.extend(s2)
AttributeError: 'set' object has no attribute 'extend'
>>> s2.add(7,8)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    s2.add(7,8)
TypeError: add() takes exactly one argument (2 given)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> s1.update({10,11,12})
>>> s1
{1, 2, 3, 10, 11, 12}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
