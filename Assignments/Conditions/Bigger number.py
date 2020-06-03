# function max(a,b)returns bigger num

def max(a,b):
	if a>b:
		return a
	else:
		return b


print("greater number ="+str(max(2,3)))

# function max(a,b,c)returns bigger num

def max1(a,b,c):
	if a>b and a>c:
		return a
	elif a>b and c>a:
		return c
	elif b>a and b>c:
		return b
	else:
		return c
print("greater number="+str(max1(2,3,4)))


# function max(a,b,c)returns bigger num

def max2(a,b,c):
	if max(a,b)>c:
		return max(a,b)
	else:
		return c
print("greater number="+str(max2(2,3,4)))


# function max(a,b,c)returns bigger num

def max3(a,b,c):
	d=max(a,b)
	return max(d,c)

print("greater number="+str(max3(2,3,4)))


# function max(a,b,c)returns bigger num
	
def max3(a,b,c):
	return max(max(a,b),c)

print("greater number="+str(max3(2,3,4)))