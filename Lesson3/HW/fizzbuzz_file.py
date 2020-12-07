with open('fizzbuzz_number.txt') as num_data, open('fizzbuzz_answer.txt', 'w') as ans_data:
    for line in num_data:
        fizz, buzz, the_end = [int(i) for i in line.strip().split(', ')]
        for j in range(1, the_end + 1):
            if j % fizz == 0 and j % buzz == 0:
                ans_data.write('FB ')
            elif j % fizz == 0:
                ans_data.write('F ')
            elif j % buzz == 0:
                ans_data.write('B ')
            else:
                ans_data.write(str(j) + ' ')
        ans_data.write('\n')