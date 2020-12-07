with open('fizzbuzz_number.txt') as num_data:
    for line in num_data:
        fizz, buzz, the_end = [int(i) for i in line.strip().split(', ')]
        for i in range(1, the_end + 1):
            if i % fizz == 0 and i % buzz == 0:
                print('FB', end=' ')
            elif i % fizz == 0:
                print('F', end=' ')
            elif i % buzz == 0:
                print('B', end=' ')
            else:
                print(i, end=' ')
        print()
