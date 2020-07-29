square2 = lambda x: x ** 2
print(square2(5))

print((lambda x: x ** 2)(5))

numbers = [1, 56, -46, 0, 36, -98]


def positive(num_list):
    pos = list()
    for i in num_list:
        if i > 0:
            pos.append(i)
    return pos


def negative(num_list):
    neg = list()
    for i in num_list:
        if i < 0:
            neg.append(i)
    return neg


def even(num_list):
    eve = list()
    for i in num_list:
        if i % 2 == 0:
            eve.append(i)
    return eve


def operations(num_list, fn):
    output = list()
    for i in num_list:
        if fn(i):
            output.append(i)
    return output


print(positive(numbers))
print(negative(numbers))
print(even(numbers))
print(operations(numbers, lambda x: x > 0))
print(operations(numbers, lambda x: x < 0))
print(operations(numbers, lambda x: x % 2 == 0))
print(list(filter(lambda x: x > 0, numbers)))
print(list(filter(lambda x: x < 0, numbers)))
print(list(filter(lambda x: x % 2 == 0, numbers)))
print(list(map(lambda x: x > 0, numbers)))
