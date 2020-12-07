print('Welcome' if int(input('Put your age ')) > 17 else 'Sorry you are to young ')

print('Good job' if input('Put something ') != '' else 'Successfully failed')

number = int(input('Put number from 1 to 100 but not divisible by 7 '))
print(f'Number {number} fits' if 1 <= number <= 100 and number % 7 != 0 else 'Sorry. Maybe next time')

year = int(input('Put some year '))
print(f'{year} is a leap year' if year % 4 == 0 and not(year % 100 == 0) or year % 400 == 0 else f'{year} is a not leap year' )

a, b = (input('Put your fist number '), input('Put your second number ')) if input('Do you have two number? Enter yes or no ') == 'yes' else (input('Put you number '), None)
print(f'Your numbers {a} and {b}' if b else f'Your number {a}')