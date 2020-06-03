# 1. Create a function that takes a list of numbers and returns a dictionary with each number as key
# and their count as value
# e.g, input = [1,2,3,4,1,1,2]; output = {1: 3, 2:2, 3:1, 4:1}
# 1 is repeated 3 times, 2 is repeated 2 times, 3 and 4 are present only once.

def count(original):
    unique = list(set(original))
    value = {}
    for key in unique:
        value[key] = 0
    for key in original:
        value[key] = value[key] + 1
    return value


print(count([1, 2, 3, 4, 1, 1, 2]))


# 2. Create a function that takes a dictionary that has student names as key and their marks as value,
# return student with maximum mark
# input {'vishnu':99, 'swetha': 100, karthik:'70'}; output: 'swetha'

def maxmark(marks):
    marklist = []
    for name in marks:
        marklist.append(marks[name])

    highmark = 0
    for i in range(len(marklist)):
        if marklist[i] >= highmark:
            highmark = marklist[i]
    return highmark


def topper(marks):
    highmark = maxmark(marks)
    toppers = []
    for student in marks:
        if marks[student] == highmark:
            toppers.append(student)
    return toppers


print("Toppers=", topper({'vishnu': 99, 'swetha': 100, 'karthik': 70}))
print("Toppers=", topper({'vishnu': 90, 'swetha': 80, 'karthik': 97, 'sruthi': 97}))
print("Toppers=", topper({'vishnu': 0, 'swetha': 0, 'karthik': 0, 'sruthi': 0}))


# 3. Create a function that takes a dictionary that has student names as key and their marks as value,
# return all the students and their marks if they have more than or equal 50
# input {'vishnu':99, 'swetha': 100, karthik:'40'}; output: {'vishnu':99, 'swetha':100}

def aboveavg1(marks):
    above50 = []
    for student in marks:
        if marks[student] >= 50:
            above50.append(student)
    return above50


def aboveavg2(marks):
    if not aboveavg1(marks):
        return "None got above 50 marks"
    else:
        return aboveavg1(marks)


print(aboveavg2({'vishnu': 99, 'swetha': 100, 'karthik': 40}))
print(aboveavg2({'vishnu': 49, 'swetha': 30, 'karthik': 40}))


# 4. Make question 3 generic with any pass mark n as input
# input 1 = {'vishnu':99, 'swetha': 100, karthik:'40'}, input 2 = 99
# output: {'vishnu':99, 'swetha':100} since only vishnu and swetha have marks more than or equal to 99 (input 2)

def pasmark1(marklist, passmark):
    abovepm = []
    for student in marklist:
        if marklist[student] >= passmark:
            abovepm.append(student)
        else:
            pass
    return abovepm
def pasmark2(marklist, passmark):
    if not pasmark1(marklist, passmark):
        return "None"
    else:
        return pasmark1(marklist, passmark)


print(pasmark2({'vishnu': 99, 'swetha': 100, 'karthik': 40}, 99))
print(pasmark2({'vishnu': 49, 'swetha': 30, 'karthik': 40}, 99))


# 5. Create a function that takes a dictionary that has student names as key and their subjects taken as value.
# return all students who have taken 'biology'
# input = {'vishnu': ['english', 'french', 'computer science], 'swetha': ['english', 'sanskrit', 'computer science'],
# 'karthik': ['english', 'tamil','biology']}
# output = ['karthik'] (because he only has taken 'biology')

def biology1(students):
    subjectlist = []
    namelist = []
    for name in students:
        subjectlist.append(students[name])
        namelist.append(name)

    biostudents = []
    for i in range(len(subjectlist)):
        if 'biology' in subjectlist[i]:
            biostudents.append(namelist[i])
    return biostudents
def biology2(students):
    if not biology1(students):
        return "No biology student"
    else:
        return biology1(students)


print(biology2({'vishnu': ['english', 'french', 'biology'], 'swetha': ['english', 'sanskrit', 'biology'],
                'karthik': ['english', 'tamil', 'biology']}))
print(biology2(
    {'vishnu': ['english', 'french', 'computer science'], 'swetha': ['english', 'sanskrit', 'computer science'],
     'karthik': ['english', 'tamil', 'biology']}))
print(biology2(
    {'vishnu': ['english', 'french', 'computer science'], 'swetha': ['english', 'sanskrit', 'computer science'],
     'karthik': ['english', 'tamil', 'economics']}))


# 6. Make function 5 generic with any subject.
# input 1 = {'vishnu': ['english', 'french', 'computer science], 'swetha': ['english', 'sanskrit', 'computer science'],
# 'karthik': ['english', 'tamil','biology']}, input 2 = 'computer science'
# output = ['vishnu', 'swetha']

def sub1(students, subject):
    subjectlist = []
    namelist = []
    for name in students:
        subjectlist.append(students[name])
        namelist.append(name)

    substudents = []
    for i in range(len(subjectlist)):
        if subject in subjectlist[i]:
            substudents.append(namelist[i])
    return substudents
def sub2(students, subject):
    if not sub1(students, subject):
        return "None"
    else:
        return sub1(students, subject)


print(sub2({'vishnu': ['english', 'french', 'computer science'], 'swetha': ['english', 'sanskrit', 'computer science'],
            'karthik': ['english', 'tamil', 'biology']}, 'biology'))
print(sub2({'vishnu': ['english', 'french', 'computer science'], 'swetha': ['english', 'sanskrit', 'computer science'],
            'karthik': ['english', 'tamil', 'biology']}, 'tamil'))
print(sub2({'vishnu': ['english', 'french', 'computer science'], 'swetha': ['english', 'sanskrit', 'computer science'],
            'karthik': ['english', 'tamil', 'biology']}, 'french'))
print(sub2({'vishnu': ['english', 'french', 'computer science'], 'swetha': ['english', 'sanskrit', 'computer science'],
            'karthik': ['english', 'tamil', 'biology']}, 'sanskrit'))
print(sub2({'vishnu': ['english', 'french', 'computer science'], 'swetha': ['english', 'sanskrit', 'computer science'],
            'karthik': ['english', 'tamil', 'biology']}, 'computer science'))
print(sub2({'vishnu': ['english', 'french', 'computer science'], 'swetha': ['english', 'sanskrit', 'computer science'],
            'karthik': ['english', 'tamil', 'biology']}, 'economics'))




