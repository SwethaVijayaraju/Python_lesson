#7. Create a function that takes a list that contains daily newly positively tested cases and returns True if there was ever a consistent
#decline in the curve over an interval of 3 days. (i.e the no.of infected people are declining continuously over 3 days) 
#e.g input =  [0,0,10,20,25,10,5,4,50,40] ;output = True (since there is an interval day 5,6,7(3 continuous days) had a consistent decline).
#Doesn't matter if there was a increase after that interval.
#e.g input =  [0,0,10,20,25,10,5,50,40]; output = False (there are no 3 continuous days where there is a consistent decline)    

def decline(input):
	length=len(input)
	prev=0
	inc=0
	output=[]
	for i in range(length):
		firstdec=i
		case=input[i]
		if case>=prev:
			prev=case
			inc=inc+1
		elif case<prev:
			break
	dec=0
	for j in range(length):
		prev=input[j-1]
		case=input[j]
		if j>firstdec:
			if case<prev:
				dec=dec+1
			elif case>=prev:
				break
	if inc==length:
		return "False"
	elif inc!=length:
		if dec>=3:
			return "True"
		else:
			return "False"

print(decline([0,0,10,20,25,10,5,4,50,40]))
print(decline([0,0,10,20,25,10,5,50,40]))






