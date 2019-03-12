Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nested=[[1,2,3],[4,5,6],[7,8,9]]
>>> flat=[]
>>> [num for elem in nested for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> nested=[[1,2,3],[4,5,6],[7,8,9]]
>>> flat=[]
>>> [num for elem in nested for num in flat]
[]
>>> nested=[[1,2,3],[4,5,6],[7,8,9]]
>>> [num for elem in nested for num in flat]
[]
>>> nested=[[1,2,3],[4,5,6],[7,8,9]]
>>> flat=[]
>>> [num for elem in nested for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> nested=[[1,2,3],[4,5,6],[7,8,9]]
>>> flat=[]
>>> for elem in nested:
	x=elem
	flat.append(x)

	
>>> flat
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> nested=[[1,2,3],[4,5,6],[7,8,9]]
>>> flat=[]
>>> num for elem in nested:
	x=elem
	flat.append(x)
	
SyntaxError: invalid syntax
>>> nested=[[1,2,3],[4,5,6],[7,8,9]]
>>> flat=[]
>>> for elem in nested:
	x=num in elem
	flat.append(x)

	
Traceback (most recent call last):
  File "<pyshell#28>", line 2, in <module>
    x=num in elem
NameError: name 'num' is not defined
>>> nested=[[1,2,3],[4,5,6],[7,8,9]]
>>> flat=[]
>>> num for elem in nested:
	x=num in elem
	flat.append(x)
	
SyntaxError: invalid syntax
>>> nested=[[1,2,3],[4,5,6],[7,8,9]]
>>> flat=[]
>>> for elem in nested:
	x=num in elem
	flat.append(x)nested=[[1,2,3],[4,5,6],[7,8,9]]
	
SyntaxError: invalid syntax
>>> nested=[[1,2,3],[4,5,6],[7,8,9]]
>>> flat=[]
>>> for sublist in nested:
	for item in sublist:
		flat.append(item)

		
>>> flat
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
