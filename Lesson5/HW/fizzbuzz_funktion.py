def result(fizz, buzz, j):
    if j % fizz == 0 and j % buzz == 0:
        return 'FB '
    elif j % fizz == 0:
        return 'F '
    elif j % buzz == 0:
        return 'B '
    else:
        return str(j) + ' '

with open('fizzbuzz_number.txt') as num_data, open('fizzbuzz_answer.txt', 'w') as ans_data:
    for line in num_data:
        fizz, buzz, the_end = [int(i) for i in line.strip().split(', ')]
        # for j in range(1, the_end + 1):
        #     ans_data.write(result(fizz, buzz, j))
        list(map(lambda j: ans_data.write(result(fizz, buzz, j)), range(1, the_end + 1)))
        ans_data.write('\n')
