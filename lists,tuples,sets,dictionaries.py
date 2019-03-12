Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> thislist=["apple", "banana", "cherry"]
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> print(thislist[1])
banana
>>> thislist[1]="blackcurrant"
>>> print(thislist)
['apple', 'blackcurrant', 'cherry']
>>> thislist=["apple", "banana", "cherry"]
>>> print(x)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
>>> thislist=["apple"]
>>> thislist=["banana"]
>>> thislist=["cherry"]
>>> print(x)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
>>> thislist=["apple", "banana","cherry"]
>>> print("yes, "apple" is in fruits list")
SyntaxError: invalid syntax
>>> print("yes, apple is in fruits list")
yes, apple is in fruits list
>>> for x in thislist:
	print(x)

	
apple
banana
cherry
>>> for x in "banana":
	print(x)

	
b
a
n
a
n
a
>>> for x in thislist:
	print(x)
	if x == "banana":
		break

	
apple
banana
>>> for b in thislist:
	print(x)

	
banana
banana
banana
>>> for b in thislist:
	print(b)

	
apple
banana
cherry
>>> for x in thislist:
	if x =="banana":
		continue
	print(x)

	
apple
cherry
>>> thistuple = ("apple", "banana", "cherry")
>>> rint(thistuple)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    rint(thistuple)
NameError: name 'rint' is not defined
>>> print(thistuple)
('apple', 'banana', 'cherry')
>>> thistuple[1] = "blackcurrant"
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    thistuple[1] = "blackcurrant"
TypeError: 'tuple' object does not support item assignment
>>> print(thistuple)
('apple', 'banana', 'cherry')
>>> for x in thistuple:
	print(x)

	
apple
banana
cherry
>>> if "apple" in thistuple:
	print("yes, 'apple' is in the fruits tuple")

	
yes, 'apple' is in the fruits tuple
>>> print(len(thistuple))
3
>>> del thistuple
>>> print(thistuple)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print(thistuple)
NameError: name 'thistuple' is not defined
>>> thistuple = tuple(("apple", "banana", "cherry"))
>>> print(thistuple)
('apple', 'banana', 'cherry')
>>> thisset = {"apple", "banana", "cherry"}
>>> for x in thisset:
	print(x)

	
banana
cherry
apple
>>> print("banana" in thisset)
True
>>> thisset.add("orange")
>>> print(thisset)
{'banana', 'cherry', 'apple', 'orange'}
>>> thisset.update(["orange", "mango", "grapes"])
>>> print(thisset)
{'mango', 'cherry', 'banana', 'orange', 'grapes', 'apple'}
>>> thisdict = {
	"brand": "ford",
	"model": "mustang",
	"year": 1964
	}
>>> print(thisdict)
{'brand': 'ford', 'model': 'mustang', 'year': 1964}
>>> x = thisdict["model"]
>>> 
>>> print(x)
mustang
>>> x = thisdict.get("model")
>>> print(x)
mustang
>>> thisdict["year'] = 2018
	     
SyntaxError: EOL while scanning string literal
>>> thisdict["year"] = 2018
	     
>>> x = thisdict.get("year")
	     
>>> print(x)
	     
2018
>>> for x in thisdict:
	     print(x)

	     
brand
model
year
>>> 
