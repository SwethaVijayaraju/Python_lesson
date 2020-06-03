#even or odd?

def number(num):
	if num==0:
		return "Neither even nor odd"
	elif (num%2)==0:
		return "Even"
	else:
		return "Odd"
	

print(number(0))
print(number(10))
print(number(101))



def even(num):
	return num%2==0

a=even(89)
print(a)

def odd(num):
	return not even(num)
b=odd(89)
print(b)


		