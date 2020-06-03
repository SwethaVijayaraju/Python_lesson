#write a function to check if the number is prime or not
def prime(num):
	if num==0 or num==1:
		return "Neither prime nor composite"
	else: 
		divisor=2
		while divisor<=num/2:
			if num%divisor==0:
				return "composite"
			else:
				divisor=divisor+1
		return "prime"

print(prime(0))
print(prime(1))
print(prime(2))
print(prime(3))
print(prime(4))
print(prime(9))
print(prime(7))
print(prime(15))
print(prime(49973))


#write a function to check if the number is prime or not using for loop

def prime(num):
	if num==0 or num==1:
		return "Neither prime nor composite"
	else: 
		for divisor in range(2,int(num/2)+1):
			if num%divisor==0:
				return "composite"
		return "prime"
	

print(prime(0))
print(prime(1))
print(prime(2))
print(prime(3))
print(prime(4))
print(prime(9))
print(prime(7))
print(prime(15))
print(prime(49973))


