Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> codes={"kenya":254,
	   "uganda":256,
	   "tanzania":255}
>>> codes["kenya"]
254
>>> codes["uganda"]
256
>>> codes["tanzania"]
255
>>> codes["kenya"]=250
>>> codes
{'kenya': 250, 'uganda': 256, 'tanzania': 255}
>>> codes["kenya"]=254
>>> codes
{'kenya': 254, 'uganda': 256, 'tanzania': 255}
>>> codes["rwanda"]=252
>>> codes
{'kenya': 254, 'uganda': 256, 'tanzania': 255, 'rwanda': 252}
>>> codes.pop("rwanda")
252
>>> codes
{'kenya': 254, 'uganda': 256, 'tanzania': 255}
>>> codes.keys()
dict_keys(['kenya', 'uganda', 'tanzania'])
>>> codes.values()
dict_values([254, 256, 255])
>>> for key in codes.keys():
	print(key)

	
kenya
uganda
tanzania
>>> for value in codes.values():
	print(value)

	
254
256
255
>>> m=dict()
>>> m
{}
>>> m["a"]=10
>>> m["b"]=20
>>> m
{'a': 10, 'b': 20}
>>> 
>>> a=dict()
>>> a["keys"]=range(0,10)
>>> a["values"]=range(0,10)*2
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a["values"]=range(0,10)*2
TypeError: unsupported operand type(s) for *: 'range' and 'int'
>>> a=dict()
>>> a["x"]=range(0,10)
>>> a["b"]=[x*x for x in x]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a["b"]=[x*x for x in x]
NameError: name 'x' is not defined
>>> a=dict()
>>> a["x"]=range(0,10)
>>> a["b"]=for g in x:
	
SyntaxError: invalid syntax
>>> a=dict()
>>> a["x"]=range(0,10)
>>> a
{'x': range(0, 10)}
>>> a=dict()
>>> a["x"]=range(0,10)
>>> for h in a:
	b=h*h
	a.append(b)

	
Traceback (most recent call last):
  File "<pyshell#46>", line 2, in <module>
    b=h*h
TypeError: can't multiply sequence by non-int of type 'str'
>>> a=dict()
>>> a["x"]=range(0,10)
>>> 
>>> 
>>> 
>>> 
>>> a=dict()
>>> x=range(0,10)
>>> for g in x:
	z=g*g
	print(z)

	
0
1
4
9
16
25
36
49
64
81
>>> a=["x"]
>>> a=["z"]
>>> a
['z']
>>> a=dict()
>>> a
{}
>>> x=range(0,10)
>>> for g in x:
	z=g*g
	print(z)

	
0
1
4
9
16
25
36
49
64
81
>>> z
81
>>> a=dict()
>>> x=range(0,10)
>>> for g in x:
	for c in g:
	z=g*g
	print(z)


	


	


	
	print(z)a=dict()
	
SyntaxError: expected an indented block
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a=dict()
>>> a=dict()
>>> a
