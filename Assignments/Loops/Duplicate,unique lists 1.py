#given a list, return True if the list has duplicate items. Else False.

def duplicate(numlist1):
	unilist1=[]
	duplist=[]
	for element1 in numlist1:
		if element1 not in unilist1:
			unilist1=unilist1+[element1]
		else:
			duplist=duplist+[element1]

	return duplist!=[]
		
print(duplicate([1,2,3,1,2,5]))
print(duplicate([1,2,3,4,5]))


#given a list, return only unique elements.

def unique(numlist2):
	unilist2=[]
	for element2 in numlist2:
		if element2 not in unilist2:
			unilist2=unilist2+[element2]
		else:
			None
	return unilist2

print(unique([1,2,3,3+1,5,0,0,"a","a",1.5,3/2,0.5]))

