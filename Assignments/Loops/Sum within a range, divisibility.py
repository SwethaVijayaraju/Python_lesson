#sum the numbers between 1 to 10 inclusive.

num=1
sum=0
while num<11:
	sum=sum+num
	num=num+1
	print(sum)

#sum the even numbers between 1 to 10 inclusive. 2+4+6+8+10

num=1
sum=0
while num<11:
	if (num%2)==0:
		sum=sum+num

	num=num+1
print(sum)


#check divibility of given number

def divisible(num1,num2):
	return num1%num2==0



#sum the numbers between 1 to 10 that is divisible by any number inclusive. 

def something(divisor):
	num=1
	sum=0
	while num<11:
		if (num%divisor)==0:
			sum=sum+num

		num=num+1
	return sum
print(something(2))
print(something(3))
print(something(4))
print(something(5))



#sum the numbers between num1 to num2 that is divisible by any number inclusive. 

def range(num1,num2,divisor):
	if num1>num2:
		num3=num1
		num1=num2
		num2=num3
		
	sum=0
	while num1<=num2:
		if divisible(num1,divisor):
			sum=sum+num1
		num1=num1+1
	return sum

print(range(1000,1,2))