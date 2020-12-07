print('*' * 20)
print('Examples 1')

print("Give it to me!")
number = int(input())

if (number >= 100):
    print ("Thanks, man!")
elif ((number > 10) and (number < 100)):
    print ("OK :(")
else:
    print ("WHAAAAT????")

if (number > 1000):
    print ("!!!!WOOOOWWWW!!!")
print()

print('*' * 20)
print('Examples 2')
x = 5
y = 10
z = 15
print(x < y and y <= z)
print(x < y <= z)

print('*' * 20)
print('Examples 3')
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)
print(l1 is l2)
print(l1 is not l2)

print('*' * 20)
print('Examples 4')
print(3 in l1)
print(4 in l1)
print(5 not in l1)

print('*' * 20)
print('Examples 5')
test = True
result = 'Test is True' if test else 'Test is False'
print(result) # result = 'Test is True'

print('*' * 20)
print('Examples 6')
test = True
print('ttt' if test else 'fff') # выведет ttt

print('*' * 20)
print('Examples 7')
s = input('Put smt ')
if s:
    pass
if 8 % 2:
    pass
print(bool(s), bool(8 % 2), sep='\n')

print('*' * 20)
print('Examples 8')
a = 11
if a > 10 and a < 20:
    pass
print(a > 10 and a < 20)

print('*' * 20)
print('Examples 9')
test = True
result = test and 'Test is True' or 'Test is False'
print(result)





