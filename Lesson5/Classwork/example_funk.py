# def plus(num1, num2, num3=0, *vasya, **qwqwqwq):
#     print(qwqwqwq)
#     return num1 + num2 + num3
#
# print(plus(1, 3, x = 4))

def plus(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

operations = {
    'plus': plus,
    'minus': minus
}

def operation(num1, num2, operations_dict, operation):
    return operations_dict[operation](num1, num2)

print(operation(10, 12, operations, 'plus'))
