#Write a function that calculates the factorial of a number.

def factorial(num):
	result=1
	for factor in range(2,(num+1)):
		result=result*factor
	return result
print(factorial(5))


#given a word, count the number of vowels in the word.

def vowels1(word):
	count=0
	for letter in word:
		if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
			count=count+1
	return count

print(vowels1("swetha"))


#given a word, count the number of vowels in the word.

def vowels2(word):
	count=0
	for letter in word:
		if letter in "aeiou":       #if letter in ['a','e','i'.'o','u']
			count=count+1
	return count

print(vowels2("aeiou"))


#write a function which takes the list of numbers and then counts the occurence of a certain number

def repeat(numlist1,number):
	count=0
	for element1 in numlist1:
		if element1==number:
			count=count+1
	return count

print(repeat([1,4,2,4,7,7,7,6,6,2],8))


#Write a function to find the area of circles for respective radii(given).

def cirarea(radii):
	areas=[]
	for radius in radii:
		area=(22/7)*radius**2
		areas=areas+[area]
	return areas

print(cirarea([1,2,3,4,5,6,7]))


#From the given list of numbers, return only the list of prime numbers.

def prime1(num):
	if num==0 or num==1:
		return "Neither prime nor composite"
	else: 
		for divisor in range(2,int(num/2)+1):
			if num%divisor==0:
				return "composite"
		return "prime"

def prime2(numberlist2):
	primelist=[]
	for element2 in numberlist2:
		result1=prime1(element2)
		if result1=="prime":
			primelist=primelist+[element2]
	return primelist

print(prime2([1,2,3,4,5,6,7,8,9,10]))






