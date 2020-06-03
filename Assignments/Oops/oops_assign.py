#1. Create a class called Rectangle which takes the sides a,b as input.
#e.g rect = Rectangle(5,4); rect.area() # it should return 20

class Rectangle:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	def area(self):
		return self.length*self.breadth

rect=Rectangle(5,4)
print(rect.area())
print(Rectangle(5,4).area())


#2. Create a class called Point which takes x, y coordinates as input. point1 = Point(1,2)
#Add a method called quadrant which returns the quadrant the point is in.
# point1.quadrant() # should return 1
#point2 = Point(-1,-2); point2.quadrant() # should return 3

#Add another method called distance which takes another point and returns the Euclidean distance between the two points
# point1.distance(point2) # should return 4.47. 

#Add another method called is_far which takes another point and returns True if the Euclidean distance is greater than 20.
#point1.is_far(point2) # should return False

#Add another method called slope that returns the slope of the line joining the two points
#point1.slope(point2) # should return -1, since the line joining from (1,2) and (-1, -2) has the slope 2. 


class Point:
	def __init__(self,xcoor,ycoor):
		self.xcoor=xcoor
		self.ycoor=ycoor

	def quadrant(self):
		if self.xcoor>0 and self.ycoor>0:
			return "quadrant=1"
		elif self.xcoor<0 and self.ycoor>0:
			return "quadrant=2"
		elif self.xcoor<0 and self.ycoor<0:
			return "quadrant=3"
		elif self.xcoor>0 and self.ycoor<0:
			return "quadrant=4"
		elif self.xcoor>0 and self.ycoor==0:
			return "positive x-axis"
		elif self.xcoor<0 and self.ycoor==0:
			return "negative x-axis"
		elif self.xcoor==0 and self.ycoor>0:
			return "positive y-axis"
		elif self.xcoor==0 and self.ycoor<0:
			return "negative y-axis"
		elif self.xcoor==0 and self.ycoor==0:
			return "origin"

	def distance(self,other):
		return (((other.xcoor-self.xcoor)**2)+((other.ycoor-self.ycoor)**2))**(1/2)

	def is_far(self,other):
		dist=self.distance(other)
		return dist>20

	def slope(self,other):
		return (other.ycoor-self.ycoor)/(other.xcoor-self.xcoor)

	def is_same(self,other):
		return other.xcoor==self.xcoor and other.ycoor==self.xcoor


point1=Point(1,2)
point2=Point(-1,2)
point3=Point(-1,-2)
point4=Point(1,-2)
point5=Point(1,0)
point6=Point(-1,0)
point7=Point(0,2)
point8=Point(0,-2)
point9=Point(0,0)
point10=Point(1,2)
print(point1.quadrant())
print(point2.quadrant())
print(point3.quadrant())
print(point4.quadrant())
print(point5.quadrant())
print(point6.quadrant())
print(point7.quadrant())
print(point8.quadrant())
print(point9.quadrant())

print(point1.distance(point3))
print(point1.is_far(point3))
print(point1.slope(point3))
print(point1.is_same(point10))


#3. Create a class called BankAccount which is initialized with an opening balance. acc = BankAccount(1000)
#Add a method called balance which returns the account's balance; acc.balance() # should return 1000

#Add a method called deposit which adds money to the account; acc.deposit(100)
# acc.balance() # should return 1100

#Add a method called withdraw which removes money from the account; acc.withdraw(50)
#acc.balance() # should return 1050

class Bankaccount1:

	def __init__(self,openbal):
		self.bal=openbal   #self.openbal=bal(wrong; bal not assigned in input)

	def deposit(self,deposit):
		self.bal=self.bal+deposit

	def withdraw(self,withdraw):
		self.bal=self.bal-withdraw

	def balance(self):
		return self.bal


acc1=Bankaccount1(1000)
acc1.deposit(100)
acc1.withdraw(50)
acc1.deposit(400)
print(acc1.balance())

class Bankaccount2:

	def __init__(self,openbal):
		self.bal=openbal   #self.openbal=bal(wrong; bal not assigned in input)
		self.dep=0
		self.wd=0
	def deposit(self,deposit):
		self.dep=self.dep+deposit

	def withdraw(self,withdraw):
		self.wd=self.wd+withdraw

	def balance(self):
		return self.bal+self.dep-self.wd


acc2=Bankaccount2(1000)
acc2.deposit(100)
acc2.withdraw(50)
acc2.deposit(400)
print(acc2.balance())


#4. Create a class called Person which is created with a name; e.g p = Person("vishnu")
#Add a function called eat which takes an item that the person has eaten
#p.eat("dosa"); p.eat("chutney")

#Add another function called all which returns all the items eaten by the person
#p.all() # returns a set {"dosa", "chutney"}

class Person:
	def __init__(self,name):
		self.n=name
		self.f=[]
	def eat(self,food):
		self.f.append(food)
	def all(self):
		return set(self.f)


p=Person("vishnu")
p.eat("dosa")
p.eat("chutney")
p.eat("chutney")
p.eat("podi")
print(p.all())
