Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[]
>>> for x in range(0,100):
	if x%9==0:
		a.append(x)

		
>>> a
[0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]
>>> b=[]
>>> for x in range(0,100):
	if x%11==0:
		b.append(x)

		
>>> b
[0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> c=a+b
>>> c
[0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> c.sort
<built-in method sort of list object at 0x0323CD78>
>>> sort.c
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    sort.c
NameError: name 'sort' is not defined
>>> c.sort()
>>> 
>>> c
[0, 0, 9, 11, 18, 22, 27, 33, 36, 44, 45, 54, 55, 63, 66, 72, 77, 81, 88, 90, 99, 99]
>>> for x in range(2019,2019):
	if x%4==0:
		print(x)

		
>>> 
>>> x
99
>>> for x in range(2019,2119):
	if x%4==0:
		print(x)

		
2020
2024
2028
2032
2036
2040
2044
2048
2052
2056
2060
2064
2068
2072
2076
2080
2084
2088
2092
2096
2100
2104
2108
2112
2116
>>> student1 = {"name":"Aisha",
		"YoB":1998}
>>> student2 = {"name":"Sharon",
		"YoB":1997}
>>> student3 = {"name":"Eve",
		"YoB":1999}
>>> student3 = {"name":"Naima",
		"YoB":2000}
>>> student4 = {"name":"Naima",
		"YoB":2000}
>>> student5 = {"name":"Gaya",
		"YoB":1995}
>>> student3
{'name': 'Naima', 'YoB': 2000}
>>> studenr3 = {"name":"Eve",
		"YoB":1999}
>>> student1 = {"name":"Aisha",
		"YoB":1998}
>>> student2 = {"name":"Sharon",
		"YoB":1997}
>>> student3 = {"name":"Eve",
		"YoB":1999}
>>> student4 = {"name":"Naima",
		"YoB":2000}
>>> student5 = {"name":"Gaya",
		"YoB":1995}
>>> students = [student1, student2, student3, student4, student5]
>>> students
[{'name': 'Aisha', 'YoB': 1998}, {'name': 'Sharon', 'YoB': 1997}, {'name': 'Eve', 'YoB': 1999}, {'name': 'Naima', 'YoB': 2000}, {'name': 'Gaya', 'YoB': 1995}]
>>> for student in students:
	age = 2019-student["YoB"]*365
	data = "Dear {}, you are {} days old".format(student["name"],age)
	print(data)

	
Dear Aisha, you are -727251 days old
Dear Sharon, you are -726886 days old
Dear Eve, you are -727616 days old
Dear Naima, you are -727981 days old
Dear Gaya, you are -726156 days old
>>> 
