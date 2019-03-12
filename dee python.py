Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> c1="kenya"
>>> c2="uganda"
>>> c3="tanzania"
>>> ke_code="254"
>>> ug_code="256"
>>> tz_code="255"
>>> c1
'kenya'
>>> print("{} code is {}".format(c1,ke_code))
kenya code is 254
>>> print("{} code is {}".format(c2,ug_code))
uganda code is 256
>>> print("{} code is {}".format(c3,tz_code))
tanzania code is 255
>>> print("{} code is {}\n {} code is {}\n {} code is {}".format(c1,ke_code,c2,ug_code,c3,tz_code))
kenya code is 254
 uganda code is 256
 tanzania code is 255
>>>


 
