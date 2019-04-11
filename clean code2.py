Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def data(number):
	y = []
	for x in range(1,number+1):
		y.append(x)
		z = sum(y)
	return z

>>> data(8)
36
>>> data(50)
1275
>>> data(100)
5050
>>> 
>>> 
>>> 
>>> 
>>> def data(list,number):
	a = []
	b = []
	for x in list:
		if x%number==0:
			a.append(x)
		else:
			b.append(x)
	print(a)
	print(b)

	
>>> x = range(0,10)
>>> data(x,3)
[0, 3, 6, 9]
[1, 2, 4, 5, 7, 8]
>>> x = [3,5,7,9,10,15]
>>> data(x,4)
[]
[3, 5, 7, 9, 10, 15]
>>> x = range(0,50)
>>> data(x,5)
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
[1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 41, 42, 43, 44, 46, 47, 48, 49]
>>> x = range(0,50)
>>> 
