Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=dict()
>>> x=range(10)
>>> g=[]
>>> for y on x:
	
SyntaxError: invalid syntax
>>> a=dict()
>>> x=range(10)
>>> g=[]
>>> for y in x:
	z=y*y
	g.append(z)

	
>>> g
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> a["x"]=range 10
SyntaxError: invalid syntax
>>> a["x"]=range(10)
>>> a["g"]=y*y
>>> a
{'x': range(0, 10), 'g': 81}
>>> a=dict()
>>> x=range(10)
>>> g=[]
>>> for y in x:
	z=y*y
	g.append(z)

	
>>> g
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> for x,g in a.items():
	print(x,g)

	
>>> a
{}
>>> g
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> x
range(0, 10)
>>> for x,g in a.items():
	print(x,g)

	
>>> names=["melissa","edna","david","kihara"]
>>> l=dict()
>>> for x in names:
	l[x]=len(x)

	
>>> l
{'melissa': 7, 'edna': 4, 'david': 5, 'kihara': 6}
>>> names=["melissa","edna","david","kihara"]
>>> age=[16,44,30,51]
>>> l=dict()
>>> for x in names:
	for y in age:
		l[x]=l[y]

		
Traceback (most recent call last):
  File "<pyshell#42>", line 3, in <module>
    l[x]=l[y]
KeyError: 16
>>> names=["melissa","edna","david","kihara"]
>>> age=[16,44,30,51]
>>> l=dict()
>>> for x in names:
	for y in age:
		l[x]=l(y)

		
Traceback (most recent call last):
  File "<pyshell#47>", line 3, in <module>
    l[x]=l(y)
TypeError: 'dict' object is not callable
>>> names=["melissa","edna","david","kihara"]
>>> age=[16,44,30,51]
>>> l=dict()
>>> l["x"]="names"
>>> l["y"]="age"
>>> l
{'x': 'names', 'y': 'age'}
>>> names=["melissa","edna","david","kihara"]
>>> age=[16,44,30,51]
>>> l=dict()
>>> for n, a in zip(names,age):
	print(n,a)

	
melissa 16
edna 44
david 30
kihara 51
>>> names=["melissa","edna","david","kihara"]
>>> age=[16,44,30,51]
>>> l=dict()
>>> for x in names:
	for y in age:
		l[x]=y

		
>>> l
{'melissa': 51, 'edna': 51, 'david': 51, 'kihara': 51}
>>> a=dict()
>>> x=range(10)
>>> g=[]
>>> for y in x:
	z=y*y
	g.append(z)

	
>>> g
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> for y in x:
	for b in g:
		a[y]=b

		
>>> a
{0: 81, 1: 81, 2: 81, 3: 81, 4: 81, 5: 81, 6: 81, 7: 81, 8: 81, 9: 81}
>>> 
