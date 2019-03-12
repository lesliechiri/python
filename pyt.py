Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruits=("apples,bananas,pineapple,oranges")
>>> print("loud_fruits")
loud_fruits
>>> fruits.upper()
'APPLES,BANANAS,PINEAPPLE,ORANGES'
>>> fruits.lower()
'apples,bananas,pineapple,oranges'
>>> fruits.caitalize()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    fruits.caitalize()
AttributeError: 'str' object has no attribute 'caitalize'
>>> fruits.capitalize()
'Apples,bananas,pineapple,oranges'
>>> friuts.isnumeric()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    friuts.isnumeric()
NameError: name 'friuts' is not defined
>>> fruits.isnumeric
<built-in method isnumeric of str object at 0x0383A920>
>>> fruits.isalpha()
False
>>> fruits.isnumeric()
False
>>> name="chairman"
>>> amount=30000
>>> print("{} will send leslie {} today".format(name,amount))
chairman will send leslie 30000 today
>>> 
