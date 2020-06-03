# given two numbers i,j and operation string.do the actual calculation of the two numbers and store it in another variable in the end print the result variable.

def sum(i, j):
    return i + j


def diff(i, j):
    return i - j


def product(i, j):
    return i * j


def quotient(i, j):
    if j != 0:
        return i / j
    else:
        return None


def operate(i, j, operation):
    a = operation == "Addition" or operation == "Add" or operation == "Sum"
    b = operation == "Subtraction" or operation == "Subtract" or operation == "Diff" or operation == "Difference"
    c = operation == "Multiplication" or operation == "Multiply" or operation == "Product"
    d = operation == "Division" or operation == "Divide" or operation == "Quotient"
    if a:
        answer1 = sum(i, j)
        answer2 = "i+j=j+i"
    elif b:
        answer1 = diff(i, j)
        answer2 = diff(j, i)
    elif c:
        answer1 = product(i, j)
        answer2 = "i*j=j*i"
    elif d:
        answer1 = quotient(i, j)
        answer2 = quotient(j, i)
    else:
        answer1 = answer2 = "unknown operation"

    return answer1, answer2


num1 = 10
num2 = 0
op = "Addition"
result = operate(num1, num2, op)
print(result)

op = "Subtraction"
result = operate(num1, num2, op)
print(result)

op = "Multiplication"
result = operate(num1, num2, op)
print(result)

op = "Division"
result = operate(num1, num2, op)
print(result)
