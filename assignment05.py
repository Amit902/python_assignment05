#Q1 Take an input year from user and decide whether it is a leap year or not.

year = int(input("enter years: "))
if(year % 4) == 0:
	print("Year is a leap year")
else:	
	print("Year is not leap year")
print("\n")	

#Q2 Take length and breadth input from user and check whether the dimensions are of square or rectangle. 
x = int(input("enter length: "))
y = int(input("enter bredth: "))
if x == y:
	print("The dimension is Square")
	
else:
	print("The dimension is Rectangle")
print("\n")	
	
	
#Q3 Take the input age of 3 people and determine oldest and youngest among them.

a = int(input("enter age of person1: "))
b = int(input("enter age of person2: "))
c = int(input("enter age of person3: "))
if a>b:
	if b>c: 
		print:("a is oldest")
	else:
		print:("c is oldest")
else:
	if b>c: 
		print:("b is oldest")
	else:		
		print:("b is oldest")
		
		
if a<b:
	if a<c:
		print:("a is youngest")
	else:
		print:("c is youngest")
else:		
	if b<c:
		print:("b is youngest")
	else:
		print:("c is youngest") 
	
print("\n")

	
#	Q.4- Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored, which is stored in the integer variable points(your input) points can only take on positive integer values up to 200. 
#If they've won a prize, the message should state "Congratulations! You won a [prize name]!" with the prize name. If there's no prize, the message should state "Sorry! No prize this time."

#Points	Prize
# 1-50	No Prize
# 51-150	Wooden Dog
# 151-180	Book
# 181-200	Chocolates

x = int(input("enter the score: "))
if x<=50:
	print("sorry this time no prize")
else:
	if x<=150:
		print("Congratulation..!! you won wodden dog")
	else:
		if x<=180:
		   print("Congratulation..!! you won Book")
		else:
			if x<=200:
				print("Congratulation..!! you won choclates")
			else:
				print("Invalid input")
print("\n")


#Q5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.

quantity = int(input("Enter Quantity: "))
if quantity*100 > 1000:
  print ("Cost is",(quantity*100)-(0.1*quantity*100))
else:
  print ("Cost is",quantity*100)
 
