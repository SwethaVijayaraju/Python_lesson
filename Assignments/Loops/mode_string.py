# 1. Create a function that takes a string of characters and return the most consecutively occurring character
# e.g
# input = "aaaaabbbcceeeeeeeb"
# output = e because e occurs consecutively 7 times

# 2. Return the character,  position of the first occurence and the no,of times
# input = "aaaaabbbcceeeeeeeb"
# output =( e, 10, 7) because e occurs consecutively 7 times starting at position 10

# For both if there are multiple characters with same no.of occurrences, return any one.

def mode1(word):
    count = {}
    for letter1 in word:
        if letter1 not in count:
            count[letter1] = 1
        else:
            count[letter1] = count[letter1] + 1

    reversecount = {}
    for letter3 in count:
        if count[letter3] not in reversecount:
            reversecount[count[letter3]] = [letter3]
        else:
            reversecount[count[letter3]].append(letter3)

    countlist = []
    for letter2 in count:
        countlist.append(count[letter2])

    ascending = sorted(list(set(countlist)))

    return reversecount[ascending[-1]]


print(mode1("aaaaabbbcceeeeeeeb"))
print(mode1("aaaaabbbcceeeeeb"))
print(mode1("aaaaabbbcceeeebeeeb"))   #retruns a
print(mode1("aaaaabbbacceeeebeeeb"))   #returns (a,0,5) not (a,0,6)


def mode2(word):
    characters=set(word)
    count = {}
    for letter1 in characters:
        count[letter1]=0
    for i in range(len(word)):
        letter4=word[i]
        index_history=i
        if i==0:
            count[letter4]=count[letter4]+1
            letter_history=letter4
        else:
            if letter4==letter_history:
                count[letter4]=count[letter4]+1
                letter_history=letter4
            else:
                count[letter4]=count[letter4]+1
                letter_history=letter4
                
    for j in range(len(word)):
        letter5=word[j]
        if j>=index_history:


    reversecount = {}
    for letter3 in count:
        if count[letter3] not in reversecount:
            reversecount[count[letter3]] = [letter3]
        else:
            reversecount[count[letter3]].append(letter3)

    countlist = []
    for letter2 in count:
        countlist.append(count[letter2])

    ascending = sorted(list(set(countlist)))

    return reversecount[ascending[-1]]


print(mode2("aaaaabbbcceeeeeeeb"))
print(mode2("aaaaabbbcceeeeeb"))
print(mode2("aaaaabbbcceeeebeeeb"))   #retruns a
print(mode2("aaaaabbbacceeeebeeeb"))   #returns (a,0,5) not (a,0,6)
