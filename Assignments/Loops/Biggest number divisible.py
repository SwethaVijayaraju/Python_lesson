#write a function that returns the biggest number divisible by a divisor within some range.

def biggest(num1,num2,divisor):
	bignum=None
	while num1<=num2:
		if (num1%divisor)==0:
			bignum=num1
		num1=num1+1
	return bignum
	
print(biggest(1,10,2))   #answer should be 10


#write a function that returns the biggest number divisible by a divisor within some range.

def biggest(num1,num2,divisor):
	while num2>=num1:
		if (num2%divisor)==0:
			return num2
		num2=num2-1
	
print(biggest(1,10,2))   #answer should be 10


