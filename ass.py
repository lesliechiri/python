Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nested=[[1,2,3],[4,5,6],[7,8,9]]
>>> flat=[]
>>> for sublist in nested:
	for x in sublist:
		flat.append(x)

		
>>> flat
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> nested=[[1,2,3],[4,5,6],[7,8,9]]
>>> squares=[]
>>> for sublist in nested:
	for x in sublist:
		a=x*x
		squares.append(a)

		
>>> squares
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> a=(1,2,3,4)

>>> 
