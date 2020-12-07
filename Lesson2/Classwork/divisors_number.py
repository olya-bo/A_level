digital = int(input('Put your number '))
print(f'делители числа {digital}', end=': ')
for i in range(digital):
    if digital % (i + 1) == 0:
        print(i+1, end=' ')

