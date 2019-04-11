pPython 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sum(a,b):
	answer = a+b
	return answer

>>> sum(10,15)
25
>>> sum(1000,10000)
11000
>>> sum(10)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    sum(10)
TypeError: sum() missing 1 required positional argument: 'b'
>>> sum(1000,10000,50)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    sum(1000,10000,50)
TypeError: sum() takes 2 positional arguments but 3 were given
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
>>> def multiply(a,b,c)
SyntaxError: invalid syntax
>>> def multiply(a,b,c):
	answer = a*b*c
	return answer

>>> multiply(6,7,8)
336
>>> def divide(a,b,c):
	answer = a/b/c
	return answer

>>> divide(10000,1000,100)
0.1
>>> def divide(a,b,):
	answer = a%b
	return answer

>>> modulus(100,7)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    modulus(100,7)
NameError: name 'modulus' is not defined
>>> def divide(a,b):
	answer = a%b
	return answer

>>> modulus(100,7)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    modulus(100,7)
NameError: name 'modulus' is not defined
>>> def modulus(a,b):
	answer = a%b
	return answer

>>> modulus
<function modulus at 0x036C6E40>
>>> modulus(100,7)
2
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
>>> def multiply(a,b,c):
	answer = a*b*c
	return answer

>>> multiply(6,7,8)
336
>>> def divide(a,b,c):
	answer = a/b/c
	return answer

>>> divide(10000,1000,100)
0.1
>>> def modulus(a,b):
	answer = a%b
	return answer

>>> modulus(100,7)
2
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
>>> def data(name,YoB):
	age = 2019-YoB
	print("Hello{} you are {} years old".format(name,age))

	
>>> data("diana",1995)
Hellodiana you are 24 years old
>>> def data(name,YoB):
	age = 2019-YoB
	print("Hello {} you are {} years old".format(name,age))

	
>>> data("edna",1975)
Hello edna you are 44 years old
>>> data("diana",1995)
Hello diana you are 24 years old
>>> data("sam",1968)
Hello sam you are 51 years old
>>> data("lisa",2003)
Hello lisa you are 16 years old
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
>>> def squares(numbers):
	for number in numbers:
		print(number*number)

		
>>> x = [1,2,3,4,5]
>>> y = [100,200,300,400]
>>> squares(x)
1
4
9
16
25
>>> squares(y)
10000
40000
90000
160000
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a=[]
>>> for number in numbers:
	s = number*number
	a. apend(s)

	
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    for number in numbers:
NameError: name 'numbers' is not defined
>>> a=[]
>>> for number in numbers:
	s = number*number
	a. append(s)

	
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    for number in numbers:
NameError: name 'numbers' is not defined
>>> a=[]
>>> for number in numbers:
	s = number*number
	a.append(s)

	
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    for number in numbers:
NameError: name 'numbers' is not defined
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
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def squares(numbers):
	for number in numbers:
		s = number*numbers
		a.append(s)

		
>>> return a
SyntaxError: 'return' outside function
>>> def squares(numbers):
	for number in numbers:
		s = number*numbers
		a.append(s)

		
>>> a=[]
>>> def squares(numbers):
	for number in numbers:
		s = number*numbers
		a.append(s)

		
>>> return a
SyntaxError: 'return' outside function
>>> a=[]
>>> def squares(numbers):
	for number in numbers:
		s = number*numbers
		a.append(s)

		
>>> s = [2,3,5,7]
>>> return a
SyntaxError: 'return' outside function
>>> a=[]
>>> def squares(numbers):
	for number in numbers:
		s = number*numbers
		a.append(s)

		
>>> a=[]
>>> def squares(numbers):
	for number in numbers:
		s = number*numbers
		a.append(s)
	return a

>>> s = [2,3,5,7]
>>> a
[]
>>> a=[]
>>> def squares(numbers):
	for number in numbers:
		s = number*numbers
		a.append(s)
	return a

>>> s = [2,3,5,7]
>>> def squares(numbers):
	for number in numbers:
		s = number*number
		a.append(s)
	return a

>>> a
[]
>>> def squares(numbers):
	for number in numbers:
		s = number*number
		a.append(s)
	return a

>>> s = [2,3,5,7]
>>> a
[]
>>> def squares(numbers):
	for number in numbers:
		s = number*number
		a.append(s)
	return a

>>> x = [1,2,3,4]
>>> y = [100,200,300,400]
>>> squares(x)
[1, 4, 9, 16]
>>> squares(y)
[1, 4, 9, 16, 10000, 40000, 90000, 160000]
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
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def tens(numbers):
	for number in numbers:
		s = number*10
		a.append(s)
	return a

>>> x = [1,2,3,4]
>>> y = [100,200,300,400]
>>> tens(x)
[1, 4, 9, 16, 10000, 40000, 90000, 160000, 10, 20, 30, 40]
>>> tens(y)
[1, 4, 9, 16, 10000, 40000, 90000, 160000, 10, 20, 30, 40, 1000, 2000, 3000, 4000]
>>> def tens(numbers):
	for number in numbers:
		s = number*10
		a.append(s)
	return a

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
>>> def tens(numbers):
	for x in numbers:
		s = x*10
		a.append(s)
	return a

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
>>> 
>>> 
>>> 
>>> b=[]
>>> def tens(numbers):
	for x in numbers:
		s = x*10
		a.append(s)
	return b

>>> x = [1,2,3,4]
>>> y = [100,200,300,400]
>>> 
>>> tens(x)
[]
>>> 
>>> 
>>> 
>>> 
>>> b=[]
>>> def tens(numbers):
	for x in numbers:
		s = x*10
		b.append(s)
	return b

>>> x = [1,2,3,4]
>>> y = [100,200,300,400]
>>> tens(x)
[10, 20, 30, 40]
>>> tens(y)
[10, 20, 30, 40, 1000, 2000, 3000, 4000]
>>> tens(y)
[10, 20, 30, 40, 1000, 2000, 3000, 4000, 1000, 2000, 3000, 4000]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> b=[]
>>> def tens(numbers):
	for x in numbers:
		t = x*10
		b.append(t)
	return b

>>> x = [1,2,3,4]
>>> y = [100,200,300,400]
>>> 
>>> tens(x)
[10, 20, 30, 40]
>>> tens(y)
[10, 20, 30, 40, 1000, 2000, 3000, 4000]
>>> b=[]
>>> 
>>> 
>>> 
>>> def tens(numbers):
	for x in numbers:
		t = x*10
		b.append(t)
	return b

>>> x = [5,6,7]
>>> y = [400,500,900]
>>> 
>>> 
>>> tens(x)
[50, 60, 70]
>>> tens(y)
[50, 60, 70, 4000, 5000, 9000]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> b=[]def tens(numbers):
	for x in numbers:
		t = x*10
		b.append(t)
	return b
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def tens(numbers):
	b=[]
	for x in numbers:
		t = x*10
		b.append(t)
	return b

>>> x = [5,6,7]
>>> y = [400,500,900]
>>> tens(x)
[50, 60, 70]
>>> tens(y)
[4000, 5000, 9000]
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
