# Factorial
def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n


print(factorial(5))


# 1. Create a recursive function that calculates the sum of numbers from 1 to n where n is the input
# e.g input = 5; output = 15

def sum(n):
    if n == 1:
        return 1
    return sum(n - 1) + n


print(sum(14))


# 2. Create a recursive function that calculates the sum of numbers in a list. Do it without any loops.
# e.g input = [1, 4, 5, 1, 3]; output = 14

def sumlist(numlist):
    i = len(numlist) - 1
    if i == 0:
        return numlist[0]
    return sumlist(numlist[0:i]) + numlist[i]


print(sumlist([1, 4, 5, 1, 3]))


#3. Create a recursive function that calculates the Fibonacci number of input n. 
#input = 7; output = 8
# 0,1,1,2,3,5,8,13,21,34,55,89,144,...

def fibonacci(n):
	i=0
	j=1
	sum1=0
	if n==1:
		return 0
	elif n==2:
		return 1
	else:
		while n>2:
			sum1=i+j #3rd element
			n=n-1
		return 


	if n==1:
		return 0

	return fibonacci(n-1)+
print(fibonacci(7))