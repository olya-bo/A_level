"""First variant"""
# f = open('reversed_yourself.py')
# z = f.readlines()
# f.close()
# for i in z[::-1]:
#     print(i.rstrip())

# '''Second variant'''
with open('reversed_yourself.py') as file:
    for line in reversed(file.readlines()):
        print(line.rstrip())
