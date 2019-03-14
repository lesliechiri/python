Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=dict()
>>> x=range(0,10)
>>> for y in x:
	z=y*y
	g.append(z)

	
Traceback (most recent call last):
  File "<pyshell#5>", line 3, in <module>
    g.append(z)
NameError: name 'g' is not defined
>>> a=dict()
>>> x=range(0,10)
>>> g=[]
>>> for y in x:
	z=y*y
	g.append(z)

	
>>> g
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> a=["x"]
>>> a=["g"]
>>> a
['g']
>>> a=dict()
>>> a
{}
>>> x=range(0,10)
>>> x
range(0, 10)
>>> a=dict()
>>> a=["x"]=range(0,10)
SyntaxError: can't assign to literal
>>> a["x"]=range(0,10)
>>> a["g"]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a["g"]
KeyError: 'g'
>>> a=dict()
>>> a["x"]=range(0,10)
>>> a["g"]=g
>>> a
{'x': range(0, 10), 'g': [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]}
>>> a=dict()
>>> x=range(0,10)
>>> g=dict()
>>> for y in x:
	z=y*y
	g.append(z)

	
Traceback (most recent call last):
  File "<pyshell#31>", line 3, in <module>
    g.append(z)
AttributeError: 'dict' object has no attribute 'append'
>>> a=dict()
>>> x=range(0,10)
>>> g=()for y in x:
	z=y*y
	g.append(z)
	
SyntaxError: invalid syntax
>>> a=dict()
>>> x=range(0,10)
>>> for y in x:
	z=y*y
	g.append(z)

	
Traceback (most recent call last):
  File "<pyshell#38>", line 3, in <module>
    g.append(z)
AttributeError: 'dict' object has no attribute 'append'
>>> a=dict()
>>> x=range(0,10)
>>> g=[]
>>> for y in x:
	z=y*y
	g.append(z)

	
>>> g
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> g=dict()
>>> g
{}
>>> g
{}
>>> a=dict()
>>> x=range(0,10)
>>> g=[]
>>> a=dict()
>>> x=range(0,10)
>>> g=dict()
>>> for y in x:
	z=y*y
	g.append(z)

	
Traceback (most recent call last):
  File "<pyshell#55>", line 3, in <module>
    g.append(z)
AttributeError: 'dict' object has no attribute 'append'
>>> a=dict()
>>> x=range(0,10)
>>> g=[]
>>> for y in x:
	z=y*y
	g.append(z)

	
>>> g
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> a["x"]=range(0,10)
>>> a["g"]=dict(g)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a["g"]=dict(g)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> a=dict()
>>> x=range(0,10)
>>> g=[]
>>> for y in x:
	z=y*y
	g.append(z)

	
>>> g
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> a=dict()
>>> a[x]=g
>>> a
{range(0, 10): [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]}
>>> a=dict()
>>> a[x]={g}
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a[x]={g}
TypeError: unhashable type: 'list'
>>> a=dict()
>>> x=range(0,10)
>>> g=[]
>>> for y in x:
	z=y*y
	g.append(z)

	
>>> g
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> a["x"]
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a["x"]
KeyError: 'x'
>>> a["x"]=range(0,10)
>>> a["g"]=x*2
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    a["g"]=x*2
TypeError: unsupported operand type(s) for *: 'range' and 'int'
>>> a["x"]=range(0,10)
>>> a["g"]=
SyntaxError: invalid syntax
>>> a["x"]=range(0,10)
>>> a=dict()
>>> x=range(0,10)
>>> a=dict()
>>> a[x]=x*x
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    a[x]=x*x
TypeError: unsupported operand type(s) for *: 'range' and 'range'
>>> a=dict()
>>> x=range(0,10)
>>> for g in range(10):
	a[g]=g*g

	
>>> a
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> fruits=["mango","melon","pineapple","peach","kiwi","avocado","orange","cantelope","apple","banana"]
>>> x=dict()
>>> x["fruits"]=len(fruits)
>>> x
{'fruits': 10}
>>> x=dict()
>>> y="fruits"
>>> x[y]=len(y)
>>> x
{'fruits': 6}
>>> fruits=["mango","melon","pineapple","peach","kiwi","avocado","orange","cantelope","apple","banana"]
>>> x=dict()
>>> for y in fruits:
	x[y]=len[y]

	
Traceback (most recent call last):
  File "<pyshell#114>", line 2, in <module>
    x[y]=len[y]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> x=dict()
>>> y="fruits"
>>> for y in fruits:
	x[y]=len[y]

	
Traceback (most recent call last):
  File "<pyshell#118>", line 2, in <module>
    x[y]=len[y]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> x=dict()
>>> y="fruits"
>>> 
>>> 
>>> 
>>> x=dict()
>>> fruits=["mango","melon","pineapple","peach","kiwi","avocado","orange","cantelope","apple","banana"]
>>> for y in fruits:
	for a in y:
		x[y]=len[y]

		
Traceback (most recent call last):
  File "<pyshell#133>", line 3, in <module>
    x[y]=len[y]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> for y in fruits:
	x[y]=len[y]

	
Traceback (most recent call last):
  File "<pyshell#135>", line 2, in <module>
    x[y]=len[y]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> x=dict()
>>> fruits=["mango","melon","pineapple","peach","kiwi","avocado","orange","cantelope","apple","banana"]
>>> for y in fruits:
	x[y]=len[y]

	
Traceback (most recent call last):
  File "<pyshell#139>", line 2, in <module>
    x[y]=len[y]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> x=dict()
>>> fruits=["mango","melon","pineapple","peach","kiwi","avocado","orange","cantelope","apple","banana"]
>>> for y in fruits:
	x[y]=len[y]
	print(x)

	
Traceback (most recent call last):
  File "<pyshell#144>", line 2, in <module>
    x[y]=len[y]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> x=dict()
>>> fruits=["mango","melon","pineapple","peach","kiwi","avocado","orange","cantelope","apple","banana"]
>>> for y in fruits:
	x[y]=len(y):
		
SyntaxError: invalid syntax
>>> x=dict()
>>> fruits=["mango","melon","pineapple","peach","kiwi","avocado","orange","cantelope","apple","banana"]
>>> for y in fruits:
	x[y]=len(y)

	
>>> x
{'mango': 5, 'melon': 5, 'pineapple': 9, 'peach': 5, 'kiwi': 4, 'avocado': 7, 'orange': 6, 'cantelope': 9, 'apple': 5, 'banana': 6}
>>> 
