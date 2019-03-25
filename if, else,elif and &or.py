Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> customer1 = {"name":"sharon",
		 "balance":400}
>>> customer2 = {"name":"eva",
		 "balance":2500}
>>> customer3 = {"name":"mercy",
		 "balance":300}
>>> customer4 = {"name":"sam",
		 "balance":100000}
>>> customer5 = {"name":"edna",
		 "balance":150000}
>>> customers = [customer1,customer2,customer3,customer4,customer5]
>>> customers
[{'name': 'sharon', 'balance': 400}, {'name': 'eva', 'balance': 2500}, {'name': 'mercy', 'balance': 300}, {'name': 'sam', 'balance': 100000}, {'name': 'edna', 'balance': 150000}]
>>> for customer in customers:
	sms = "Hi {},your balance is {}".format(customer["name"],customer["balance"])

	
>>> sms
'Hi edna,your balance is 150000'
>>> for customer in customers:
	sms = "Hi {},your balance is {}".format(customer["name"],customer["balance"])
	print(sms)

	
Hi sharon,your balance is 400
Hi eva,your balance is 2500
Hi mercy,your balance is 300
Hi sam,your balance is 100000
Hi edna,your balance is 150000
>>> for customer in customers:
	loan = customer["balance"]/2.9:
		
SyntaxError: invalid syntax
>>> for customer in customers:
	loan = customer["balance"]/2.9
	sms = "Dear {},your loan limit is {}".format(customer["name"],customer["balance/2.9"])
	print(sms)

	
Traceback (most recent call last):
  File "<pyshell#24>", line 3, in <module>
    sms = "Dear {},your loan limit is {}".format(customer["name"],customer["balance/2.9"])
KeyError: 'balance/2.9'
>>> for customer in customers:
	loan = customer["balance"]/2.9
	sms = "Dear {},your loan limit is {}".format(customer["name"],"loan"])
	print(sms)
	
SyntaxError: invalid syntax
>>> for customer in customers:
	loan = customer["balance"]/2.9
	sms = "Dear {},your loan limit is {}".format(customer["name"],"loan")
	print(sms)

	
Dear sharon,your loan limit is loan
Dear eva,your loan limit is loan
Dear mercy,your loan limit is loan
Dear sam,your loan limit is loan
Dear edna,your loan limit is loan
>>> for customer in customers:
	loan = customer["balance"]/2.9
	print(loan)
	for customer in customers:
		loan = customer["balance"]/2.9
		sms = "Dear {},your loan limit is {}".format(customer["name"],loan)
		print(sms)

		
137.93103448275863
Dear sharon,your loan limit is 137.93103448275863
Dear eva,your loan limit is 862.0689655172414
Dear mercy,your loan limit is 103.44827586206897
Dear sam,your loan limit is 34482.75862068966
Dear edna,your loan limit is 51724.137931034486
862.0689655172414
Dear sharon,your loan limit is 137.93103448275863
Dear eva,your loan limit is 862.0689655172414
Dear mercy,your loan limit is 103.44827586206897
Dear sam,your loan limit is 34482.75862068966
Dear edna,your loan limit is 51724.137931034486
103.44827586206897
Dear sharon,your loan limit is 137.93103448275863
Dear eva,your loan limit is 862.0689655172414
Dear mercy,your loan limit is 103.44827586206897
Dear sam,your loan limit is 34482.75862068966
Dear edna,your loan limit is 51724.137931034486
34482.75862068966
Dear sharon,your loan limit is 137.93103448275863
Dear eva,your loan limit is 862.0689655172414
Dear mercy,your loan limit is 103.44827586206897
Dear sam,your loan limit is 34482.75862068966
Dear edna,your loan limit is 51724.137931034486
51724.137931034486
Dear sharon,your loan limit is 137.93103448275863
Dear eva,your loan limit is 862.0689655172414
Dear mercy,your loan limit is 103.44827586206897
Dear sam,your loan limit is 34482.75862068966
Dear edna,your loan limit is 51724.137931034486
>>> for customer in customers:
	loan = customer["balance"]/2.9
	sms = "dear {},your loan limit is {}".format(customer["name"],loan)
	print(sms)

	
dear sharon,your loan limit is 137.93103448275863
dear eva,your loan limit is 862.0689655172414
dear mercy,your loan limit is 103.44827586206897
dear sam,your loan limit is 34482.75862068966
dear edna,your loan limit is 51724.137931034486
>>> for customer in customers:
	loan = customer["balance"]/2.9
	sms = "Dear {},your loan limit is {}".format(customer["name"],loan)
	print(sms)

	
Dear sharon,your loan limit is 137.93103448275863
Dear eva,your loan limit is 862.0689655172414
Dear mercy,your loan limit is 103.44827586206897
Dear sam,your loan limit is 34482.75862068966
Dear edna,your loan limit is 51724.137931034486
>>> 
>>> 
>>> for customer in customers:
	loan = customer["balance"]//2.9
	sms = "Dear {},your loan limit is {}".format(customer["name"],loan)
	print(sms)

	
Dear sharon,your loan limit is 137.0
Dear eva,your loan limit is 862.0
Dear mercy,your loan limit is 103.0
Dear sam,your loan limit is 34482.0
Dear edna,your loan limit is 51724.0
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> for x in range(0,10):
	if x%3==0:
		print(x)

		
0
3
6
9
>>> for x in range(0,10):
	if x/3>=1:
		print(x)

		
3
4
5
6
7
8
9
>>> for x in range(0,10):
	if x%3>=1:
		print(x)

		
1
2
4
5
7
8
>>> for x in range(0,10):
	if x%3!=0:
		print(x)

		
1
2
4
5
7
8
>>> for x in range(0,10):
	if x%3>0:
		print(x)

		
1
2
4
5
7
8
>>> for x in range(0,10):
	if x%3==0:
		print("{} is divisible by 3".format(x))
	else:
		print("{} is not divisible by 3".format(x))

		
0 is divisible by 3
1 is not divisible by 3
2 is not divisible by 3
3 is divisible by 3
4 is not divisible by 3
5 is not divisible by 3
6 is divisible by 3
7 is not divisible by 3
8 is not divisible by 3
9 is divisible by 3
>>> 
>>> 
>>> 
>>> 
>>> 
>>> for x in range(0,20):
	if x%3==0:
		print("{} is divisible by 3".format(x))
	elif x%5==0:
		print("{} is divisible by 5".format(x))
	else:
		print("{} is not divisible by 3 or 5".format(x))

		
0 is divisible by 3
1 is not divisible by 3 or 5
2 is not divisible by 3 or 5
3 is divisible by 3
4 is not divisible by 3 or 5
5 is divisible by 5
6 is divisible by 3
7 is not divisible by 3 or 5
8 is not divisible by 3 or 5
9 is divisible by 3
10 is divisible by 5
11 is not divisible by 3 or 5
12 is divisible by 3
13 is not divisible by 3 or 5
14 is not divisible by 3 or 5
15 is divisible by 3
16 is not divisible by 3 or 5
17 is not divisible by 3 or 5
18 is divisible by 3
19 is not divisible by 3 or 5
>>> 
>>> 
>>> for x in range(0,100):
	if x%7==0:
		print(x)

		
0
7
14
21
28
35
42
49
56
63
70
77
84
91
98
>>> for x in range(0,100):
	if x%7==0:
		print("{} is divisible by 7".format(x))
	else:
		print("{} is not divisible by 7".format(x))

		
0 is divisible by 7
1 is not divisible by 7
2 is not divisible by 7
3 is not divisible by 7
4 is not divisible by 7
5 is not divisible by 7
6 is not divisible by 7
7 is divisible by 7
8 is not divisible by 7
9 is not divisible by 7
10 is not divisible by 7
11 is not divisible by 7
12 is not divisible by 7
13 is not divisible by 7
14 is divisible by 7
15 is not divisible by 7
16 is not divisible by 7
17 is not divisible by 7
18 is not divisible by 7
19 is not divisible by 7
20 is not divisible by 7
21 is divisible by 7
22 is not divisible by 7
23 is not divisible by 7
24 is not divisible by 7
25 is not divisible by 7
26 is not divisible by 7
27 is not divisible by 7
28 is divisible by 7
29 is not divisible by 7
30 is not divisible by 7
31 is not divisible by 7
32 is not divisible by 7
33 is not divisible by 7
34 is not divisible by 7
35 is divisible by 7
36 is not divisible by 7
37 is not divisible by 7
38 is not divisible by 7
39 is not divisible by 7
40 is not divisible by 7
41 is not divisible by 7
42 is divisible by 7
43 is not divisible by 7
44 is not divisible by 7
45 is not divisible by 7
46 is not divisible by 7
47 is not divisible by 7
48 is not divisible by 7
49 is divisible by 7
50 is not divisible by 7
51 is not divisible by 7
52 is not divisible by 7
53 is not divisible by 7
54 is not divisible by 7
55 is not divisible by 7
56 is divisible by 7
57 is not divisible by 7
58 is not divisible by 7
59 is not divisible by 7
60 is not divisible by 7
61 is not divisible by 7
62 is not divisible by 7
63 is divisible by 7
64 is not divisible by 7
65 is not divisible by 7
66 is not divisible by 7
67 is not divisible by 7
68 is not divisible by 7
69 is not divisible by 7
70 is divisible by 7
71 is not divisible by 7
72 is not divisible by 7
73 is not divisible by 7
74 is not divisible by 7
75 is not divisible by 7
76 is not divisible by 7
77 is divisible by 7
78 is not divisible by 7
79 is not divisible by 7
80 is not divisible by 7
81 is not divisible by 7
82 is not divisible by 7
83 is not divisible by 7
84 is divisible by 7
85 is not divisible by 7
86 is not divisible by 7
87 is not divisible by 7
88 is not divisible by 7
89 is not divisible by 7
90 is not divisible by 7
91 is divisible by 7
92 is not divisible by 7
93 is not divisible by 7
94 is not divisible by 7
95 is not divisible by 7
96 is not divisible by 7
97 is not divisible by 7
98 is divisible by 7
99 is not divisible by 7
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
>>> for x in range(0,20):
	if x%3==0 and x%5==0:
		print(x)

		
0
15
>>> for x in range(0,20):
	if x%3==0 or x%5==0:
		print(x)

		
0
3
5
6
9
10
12
15
18
>>> true and true
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    true and true
NameError: name 'true' is not defined
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
>>> True or True
True
>>> True or False
True
>>> False or True
True
>>> False or False
False
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> for x in range(0,20):
	if x%3==0:
	    print("{} is divisible by 3".format(x))
			elif x%5==0:
				print("{} is divisible by 5".format(x))
			else:
				print("{} is not divisible by 3 or 5".format(x))
				
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for x in range(900,950):
	if x%3==0:
		print("buzz".format(x))
	elif x%5==0:
		print("fizz".format(x))
	if x%3==0 0r x%5==0:
		
SyntaxError: invalid syntax
>>> for x in range(900,950):
	if x%3==0:
		print("buzz".format(x))
	elif x%5==0:
		print("fizz".format(x))
	if x%3==0 or x%5==0:
		print("fizzbuzz").format(x))
		
SyntaxError: invalid syntax
>>> for x in range(900,950):
	if x%3==0:
		print("buzz".format(x))
	elif x%5==0:
		print("fizz".format(x))
	if x%3==0 or x%5==0:
		print("fizzbuzz".format(x))
	else:
		print(x)

		
buzz
fizzbuzz
901
902
buzz
fizzbuzz
904
fizz
fizzbuzz
buzz
fizzbuzz
907
908
buzz
fizzbuzz
fizz
fizzbuzz
911
buzz
fizzbuzz
913
914
buzz
fizzbuzz
916
917
buzz
fizzbuzz
919
fizz
fizzbuzz
buzz
fizzbuzz
922
923
buzz
fizzbuzz
fizz
fizzbuzz
926
buzz
fizzbuzz
928
929
buzz
fizzbuzz
931
932
buzz
fizzbuzz
934
fizz
fizzbuzz
buzz
fizzbuzz
937
938
buzz
fizzbuzz
fizz
fizzbuzz
941
buzz
fizzbuzz
943
944
buzz
fizzbuzz
946
947
buzz
fizzbuzz
949
>>> for x in range(900,950):
	if x%3==0 and x%5==0:
		print("fizzbuzz".format(x))
	if x%5==0:
		print("fizz".format(x))
	if x%3==0:
		print("buzz".format(x))
	else:
		print(x)

		
fizzbuzz
fizz
buzz
901
902
buzz
904
fizz
905
buzz
907
908
buzz
fizz
910
911
buzz
913
914
fizzbuzz
fizz
buzz
916
917
buzz
919
fizz
920
buzz
922
923
buzz
fizz
925
926
buzz
928
929
fizzbuzz
fizz
buzz
931
932
buzz
934
fizz
935
buzz
937
938
buzz
fizz
940
941
buzz
943
944
fizzbuzz
fizz
buzz
946
947
buzz
949
>>> for x in range(900,950):
	if x%3==0 and x%5==0:
		print("fizzbuzz".format(x))
	elif x%5==0:
		print("fizz".format(x))
	elif x%3==0:
		print("buzz".format(x))
	else:
		print(x)

		
fizzbuzz
901
902
buzz
904
fizz
buzz
907
908
buzz
fizz
911
buzz
913
914
fizzbuzz
916
917
buzz
919
fizz
buzz
922
923
buzz
fizz
926
buzz
928
929
fizzbuzz
931
932
buzz
934
fizz
buzz
937
938
buzz
fizz
941
buzz
943
944
fizzbuzz
946
947
buzz
949
>>> for x in range(900,950):
	if x%3==0 and x%5==0:
		print("fizzbuzz")
	elif x%5==0:
		print("fizz")
	elif x%3==0:
		print("buzz")
	else:
		print(x)

		
fizzbuzz
901
902
buzz
904
fizz
buzz
907
908
buzz
fizz
911
buzz
913
914
fizzbuzz
916
917
buzz
919
fizz
buzz
922
923
buzz
fizz
926
buzz
928
929
fizzbuzz
931
932
buzz
934
fizz
buzz
937
938
buzz
fizz
941
buzz
943
944
fizzbuzz
946
947
buzz
949
>>> 
