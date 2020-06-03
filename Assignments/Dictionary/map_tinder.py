# 7. Create a function which takes a dictionary that has student name and their crush name as value.
# Return who is the most crushed.
# input = {'vishnu':'swetha', 'karthik': 'swetha', 'sukrut': 'shreya'}
# output = 'swetha' because she has 2 people who have crush on her.


def popularity(crushlist):
    popularppl = []
    for admirer in crushlist:
        popularppl.append(crushlist[admirer])

    countmap = {}
    for person1 in popularppl:
        if person1 not in countmap:
            countmap[person1] = 1
        elif person1 in countmap:
            countmap[person1] = countmap[person1] + 1

    countlist = []
    for person2 in countmap:
        countlist.append(countmap[person2])

    ascending = sorted(countlist)

    mostcrushed = []
    for person3 in countmap:
        if ascending[-1] == countmap[person3]:
            mostcrushed.append(person3)

    return mostcrushed


print(popularity({'vishnu': 'swetha', 'karthik': 'swetha', 'sukrut': 'shreya'}))
print(popularity({'vishnu': 'swetha', 'karthik': 'jessie', 'sukrut': 'shreya'}))
print(popularity({'vishnu': 'swetha', 'karthik': 'swetha', 'simbu': 'jessie', 'sukrut': 'shreya', 'roy': 'jessie'}))


# 8. Create a function which takes a dictionary that has student name and their crush name as value.
# Return all the mutual matches (Tinder!!!)
# input = {'vishnu':'swetha', 'karthik': 'swetha', 'swetha':'vishnu', 'surkrut':'shreya', 'shreya': 'sukrut'}
# output = [('vishnu','swetha'), ('shreya','sukrut')]. Returns a list with pair as tuples.
# Don't worry about ordering. Poor karthik one sided love.

def tinder(matchlist):
    posspairs = []
    for name in matchlist:
        posspairs.append(frozenset([name, matchlist[name]]))
    couplemap = {}
    for pair1 in posspairs:
        if pair1 not in couplemap:
            couplemap[pair1] = 1
        elif pair1 in couplemap:
            couplemap[pair1] = couplemap[pair1] + 1
    couple = []
    for pair2 in couplemap:
        if couplemap[pair2] == 2:
            couple.append(tuple(pair2))
    return couple


print(tinder({'vishnu': 'swetha', 'karthik': 'swetha', 'swetha': 'vishnu', 'sukrut': 'shreya', 'shreya': 'sukrut'}))
print(
    tinder({'simbu': 'nayanthara', 'nayanthara': 'vignesh', 'vignesh': 'tamana', 'tamana': 'simbu', 'shreya': 'jeeva'}))


# 9. Create a function which takes a dictionary that has student name and their crush name as value.
# Return a dictionary which contains student names and who has a crush on them as value. Basically the reverse.
# input = {'vishnu':'swetha', 'karthik': 'swetha', 'sukrut': 'shreya'}
# output = {'swetha': ['vishnu', 'karthik'], 'shreya': ['sukrut']}
# swetha is liked by vishnu and karthik, since she is the crush for both. The values are list because one person
# can be liked by more than one person.

def famous(crushlist):
    admirerlist = {}
    for admirer in crushlist:
        admiree = crushlist[admirer]
        if admiree not in admirerlist:
            admirerlist[admiree] = [admirer]
        else:
            admirerlist[admiree].append(admirer)
    return admirerlist


print(famous({'vishnu': 'swetha', 'karthik': 'swetha', 'sukrut': 'shreya'}))
print(famous({'vishnu': 'swetha', 'karthik': 'jessie', 'sukrut': 'shreya'}))
print(famous({'vishnu': 'swetha', 'karthik': 'swetha', 'swetha': 'vishnu', 'buvana': 'vishnu', 'sukrut': 'shreya'}))


# 10. input = {'simbu': ['nayanthara','hansika'], 'nayanthara':['vignesh','simbu','dhanush'], 'vignesh': ['nayanthara'],
# 'shreya': ['jeeva']}
# output = {#nayan:[simbu,vignesh],hansika:[simbu],vignesh:[nayan],simbu:[nayan],dhanush:[nayan],jeeva:[shreya]

def playhuman(playlist):
    admirerlist = {}
    for admirer in playlist:
        admireelist = playlist[admirer]
        for admiree in admireelist:
            if admiree not in admirerlist:
                admirerlist[admiree] = [admirer]
            else:
                admirerlist[admiree].append(admirer)
    return admirerlist


print(playhuman(
    {'simbu': ['nayanthara', 'hansika'], 'nayanthara': ['vignesh', 'simbu', 'dhanush'], 'vignesh': ['nayanthara'],
     'shreya': ['jeeva']}))

# print(circlelove({'simbu': 'nayanthara', 'nayanthara': 'vignesh', 'vignesh': 'tamana', 'tamana': 'simbu'}))
# learn later
