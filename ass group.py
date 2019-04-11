Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> customer1 = {"name":"Irene",
		 "loan":50000}
>>> customer2 = {"name":"Joy",
		 "loan":80000}
>>> customer3 = {"name":"Beatrice",
		 "loan":70000}
>>> customer4 = {"name":"Cate",
		 "loan":60000}
>>> customer4 = {"name":"shee",
		 "loan":40000}
>>> customers = [customer1,customer2,customer3,customer4,customer5]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    customers = [customer1,customer2,customer3,customer4,customer5]
NameError: name 'customer5' is not defined
>>> customer1 = {"name":"Irene",
		 "loan":50000}
>>> customer2 = {"name":"Joy",
		 "loan":80000}
>>> customer3 = {"name":"Beatrice",
		 "loan":70000}
>>> customer4 = {"name":"Cate",
		 "loan":60000}
>>> customer5 = {"name":"shee",
		 "loan":40000}
>>> customers = [customer1,customer2,customer3,customer4,customer5]
>>> 
>>> 
>>> 
>>> 
>>> for customer in customers:
	balance = (15/100)*customer["loan]
				    
SyntaxError: EOL while scanning string literal
>>> for customer in customers:
	balance = (15/100)*customer["loan"]

				    
>>> 
				    
>>> 
				    
>>> customer1 = {"name":"Irene",
		 "loan":50000}
				    
>>> customer2 = {"name":"Joy",
		 "loan":80000}
				    
>>> customer3 = {"name":"Beatrice",
		 "loan":70000}
				    
>>> customer5 = {"name":"shee",
		 "loan":40000}
				    
>>> customer4 = {"name":"Cate",
		 "loan":60000}
				    
>>> customers = [customer1,customer2,customer3,customer4,customer5]
				    
>>> for customer in customers:
	balance = (15/100)*customer["loan]
				    
SyntaxError: EOL while scanning string literal
>>> for customer in customers:
	balance = (15/100)*customer["loan"]
	data = "dear {} ,interest accumulated by loan is {}".format(customer["name"],balance)
	print(data)

				    
dear Irene ,interest accumulated by loan is 7500.0
dear Joy ,interest accumulated by loan is 12000.0
dear Beatrice ,interest accumulated by loan is 10500.0
dear Cate ,interest accumulated by loan is 9000.0
dear shee ,interest accumulated by loan is 6000.0
>>> 
