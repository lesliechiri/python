Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nested=[[1,2,3],[4,5,6],[7,8,9]]
>>> flat=[]
>>> for sublist in nested:
	for item in sublist:
		flat.append(item)

		
>>> flat
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> nested=[[1,2,3],[4,5,6],[7,8,9]]
>>> flat=[]
>>> for sublist in nested:
	for item*2 in sublist:
		flat.append(item)
		
SyntaxError: can't assign to operator
>>> nested=[[1,2,3],[4,5,6],[7,8,9]]
>>> flat=[]
>>> for sublist in nested:
	for item*2 in sublist:
		flat.append(item)
		
SyntaxError: can't assign to operator
>>> nested=[[1,2,3],[4,5,6],[7,8,9]]
>>> flat=[]
>>> for sublist in nested:
	for item*item in sublist:
		flat.append(item)
		
SyntaxError: can't assign to operator
>>> nested=[[1,2,3],[4,5,6],[7,8,9]]
>>> flat=[]
>>> for sublist in nested:
	for x in sublist:
		flat.append(x)

		
>>> flat
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> nested=[[1,2,3],[4,5,6],[7,8,9]]flat=[]
SyntaxError: invalid syntax
>>> nested=[[1,2,3],[4,5,6],[7,8,9]]
>>> flat=[]
>>> for sublist in nested:
	for x in sublist:
		a=x*x
		flat.append(a)

		
>>> flat
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
