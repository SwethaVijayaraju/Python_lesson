# Return the difference of 2 given lists. eg.a=[1,2,3] and b=[1,2]. a-b=[3]
def difference1(list1, list2):
    difflist = []
    for element1 in list1:
        if element1 not in list2:
            difflist = difflist + [element1]
    return difflist


print(difference1([1, 2, 3], [1, 2]))
print(difference1([1, 2], [1, 2]))


# Return the difference of 2 given lists. eg.a=[1,2,3] and b=[1,2]. a-b=[3]
def difference2(list1, list2):
    return list(set(list1) - set(list2))


print(difference2([1, 2, 3], [1, 2]))
print(difference2([1, 2], [1, 2]))

# List indexing and list slicing

a = [1, 2, 3, 4]
print(a[0])  # gives the 1st element
print(a[:3])  # gives 1st to 3rd elements
print(a[2:])
print(a[0:4])
print(a[0:1])
print(a.append(5))
print(a)

# tuple
