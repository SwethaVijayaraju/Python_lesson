#1. Create a function that takes a list that contains daily newly positively tested cases and returns the daily increase in cases. 
#e.g input = [2,6,10,20,25]output = [2,4,4,10,5]

def dailyinc1(input):
	increase=0
	output=[]
	for case in input:
		increase=case-increase
		output=output+[increase]
		increase=case
	return output
#or
def dailyinc2(input):
	increase=0
	output=[]
	for case in input:
		output.append(case-increase)
		increase=case
	return output
#or
def dailyinc3(input):
	increase=0
	output=[]
	for i in range(len(input)):
		output.append(input[i]-increase)
		increase=input[i]
	return output

print(dailyinc1([2,6,10,20,25]))
print(dailyinc2([2,6,10,20,25]))
print(dailyinc3([2,6,10,20,25]))


#2. Create a function that takes a list that contains daily newly positively tests cases and returns the total cases so far.
#e.g input = [2,6,10,20,25];output = [2,8,18,38,63]

def totalcase1(input):
	total=0
	output=[]
	for case in input:
		total=case+total
		output.append(total)
	return output
#or
def totalcase2(input):
	total=0
	output=[]
	for i in range(len(input)):
		total=input[i]+total
		output.append(total)
	return output

print(totalcase1([2,6,10,20,25]))
print(totalcase2([2,6,10,20,25]))


#3. Create a function that takes a list that contains daily newly positively tested cases and returns the day that had most newly affected. 
#e.g input = [2,6,10,20,25,10] ; output = 4 (on 5th day there were the most infected) consider first item as 0th day. 

def dayhighest2(input):
	highest=0
	days=[]
	for i in range(len(input)):
		if input[i]==0:
			continue
		elif input[i]>highest:
			highest=input[i]
			days=[i+1]
		elif input[i]==highest:
			days.append(i+1)
	return days
def dayhighest1(input):
	if dayhighest2(input)==[]:
		return "No cases"
	else:
		return dayhighest2(input)
		
print("Day=",dayhighest1([2,6,10,20,25,10]))
print("Day=",dayhighest1([2,6,10,20,25,25]))
print("Day=",dayhighest1([20, 20, 25, 25]))
print("Day=",dayhighest1([20, 0, 29, 25]))
print("Day=",dayhighest1([0,0,0]))


#4. Create a function that takes a list that contains daily newly positively tested cases and another list that contains daily recovered
#cases, return the total active cases so far.
#e.g input 1 = [2,6,10,20,25], input 2 = [0,0,0,1,5]; output = [2,8,18,37,57]  totalcase=[2,8,18,38,63]


def activecase1(input1,input2):
	ts=totalcase2(input1)
	active=0
	position=0
	output=[]
	case2=0

	for case1 in ts:
		case2=case2+input2[position]
		active=case1-case2
		position=position+1
		output=output+[active]

	return output
#or
def activecase2(input1,input2):
	position=0
	rec=0
	output=[]
	for i in totalcase2(input1):
		rec=rec+input2[position]
		output.append(i-rec)
		position=position+1		
	return output
#or
def activecase3(input1,input2):
	if len(input1)!=len(input2):
		return "input error"
	else:
		rec=0
		output=[]
		input3=totalcase2(input1)
		for i in range(len(input3)):
			rec=rec+input2[i]
			output.append(input3[i]-rec)	
		return output

print(activecase1([2,6,10,20,25],[0,0,0,1,5]))
print(activecase2([2,6,10,20,25],[0,0,0,1,5]))
print(activecase3([2,6,10,20,25],[0,0,0,1,5]))
print(activecase3([2,6,10,20],[0,0,0,1,5]))
print(activecase3([2,6,10,20,25],[0,0,0,5]))

#5. Create a function that takes a list that contains daily newly positively tested cases and another list that contains daily recovered
#cases, return the no.of days it takes for other infected people to recover (based on the average recovery and assume no new cases are
#reported)
#input 1 = [0,0,10,20,25], input 2 = [0,0,0,1,5] ; output = 16.33 
#(1+5) / 2 = 3 avg recovery per day. ignore day 0, 1, 2 because the actual infection started on day 2.
#Remaining infected = total - already cured = 55 - 6 = 49.
#Days for remaining to recover = 49/3 = 16.33 days.

def recdays1(input1,input2):
	rec2=0
	days=0
	for case1 in input2:
		if case1!=0:
			rec2=rec2+case1
			days=days+1

	patient=rec2/days

	total1=0
	for case2 in input1:
		total1=case2+total1

	return (total1-rec2)/patient 

#or

def recperday(input2):
	rec=0
	days=0
	length=len(input2)
	for i in range(length):
		firstrec=i
		case1=input2[i]
		if case1==0:
			continue
		else:
			break
	for j in range(length):
		case2=input2[j]
		if j>=firstrec:
			rec=rec+case2
			days=days+1
		else:
			continue
	return [rec,days]

def activecases(input1):
	total=0
	for case3 in input1:
		total=case3+total
	return total

def recdays2(input1,input2):
	if len(input1)!=len(input2):
		return "input error"
	else:
		recndays=recperday(input2)
		totalcases=activecases(input1)
		patient=recndays[0]/recndays[1]
		active=totalcases-recndays[0]
		if patient==0 or active==0 or totalcases==0:
			return "Requires more data"
		else:
			return active/patient

print(recdays2([0,0,10,20,25],[0,0,0,1,5]))
print(recdays2([0,10,10,20,25],[0,0,0,1,5]))
print(recdays2([0,10,10,20,25,10,20],[0,0,0,1,5,0,6]))
print(recdays2([0,0,10,20,25],[0,0,0,0,0]))
print(recdays2([0,0,0,0,0],[0,0,0,1,5]))
print(recdays2([0,0,0,0,0],[0,0,0,0,0]))
print(recdays2([0,10,10,20,25,10,20],[0,0,0,1]))


#6. Create a function that takes a list that contains daily newly positively tested cases  and returns True if the curve is declining.
#(i.e there are always lesser no.of new cases each day after some particular day)
#e.g input = [0,0,10,20,25,10,5,4]; output = True (since after day 4, there is always a decline)
#e.g input =  [0,0,10,20,25,10,11,12]; output = False (even though day 5 had a decline, day 6 had an increase.
#So there are no days after which there is a consistent decline in cases)

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
	antidec=0
	for j in range(length):
		prev=input[j-1]
		case=input[j]
		if j>firstdec:
			if case<prev:
				continue
			elif case>=prev:
				antidec=antidec+1
	if inc==length:
		return "False"
	elif inc!=length:
		if antidec==0:
			return "True"
		elif antidec!=0:
			return "False"

print(decline([0,0,10,20,25,10,5,4]))
print(decline([0,0,10,20,25,10,11,12]))
print(decline([0,0,10,20,25,26,48,50]))
print(decline([0,0,10,20,25,26,48,43]))
print(decline([10,10,10,10]))
print(decline([10,9,7,4]))
print(decline([10,9,7,4,6,5]))
print(decline([0,9,19,18,17,15,50,39,31,25])) #check this

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



