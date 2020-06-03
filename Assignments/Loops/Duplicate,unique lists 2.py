#given a list, return True if the list has duplicate items. Else False.

def duplicate2(numlist2):
	unilist1=[]
	for element1 in numlist2:
		if element1 not in unilist1:
			unilist1=unilist1+[element1]
	return unilist1

def duplicate1(numlist1):
	return duplicate2(numlist1)!=numlist1
		
print(duplicate1([1,2,3,1,2,5]))
print(duplicate1([1,2,3,4,5]))


#given a list, return only unique elements.

def unique1(numlist3):
	return duplicate2(numlist3)
print(unique1([1,2,3,3+1,5,0,0,"a","a",1.5,3/2,0.5]))



#given a list, return True if the list has duplicate items. Else False.

def duplicate3(numlist4):
	return list(set(numlist4))!=numlist4
		
print(duplicate3([1,2,3,1,2,5]))
print(duplicate3([1,2,3,4,5]))

#given a list, return only unique elements.

def unique2(numlist5):
	return list(set(numlist5))

print(unique2([1,2,3,3+1,5,0,0,"a","a",1.5,3/2,0.5]))
