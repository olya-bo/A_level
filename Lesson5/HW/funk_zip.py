a = [1,2]
b = [3,4]
c = [5,6]
print(list(zip(a,b,c)))


name = 'cdfe'
first_name = 'aool'
last_name = 'tgxk'
animal = list(zip(name, first_name, last_name))
for i in animal:
    print(''.join(i), end=' ')
print()


names = ['Olya', 'Kolya', 'Polya', 'Julya']
last_names = ['Ivanova', 'Petrova']
while True:
    if len(names) == len(last_names):
        full_name = dict(zip(names, last_names))
        print(full_name)
        break
    elif len(last_names) > len(names):
        names.append('No name')
        continue
    else:
        last_names.append('No last_names')
        continue

letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
operators = ['*', '/', '+']
for l, n, o in zip(letters, numbers, operators):
    print(f'Letter: {l}')
    print(f'Number: {n}')
    print(f'Operator: {o}')

pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs)
print(numbers)
print(letters)



