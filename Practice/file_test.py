with open('test.txt', 'r') as text:
    for line in text:
        ans = line.rstrip().split(';')
        number_sum = [int(i) for i in ans[0].split()]
        whole_part, remainder_division = int(ans[1].split()[0]), int(ans[1].split()[1])
        if sum(number_sum) // len(number_sum) == whole_part and sum(number_sum) % len(number_sum) == remainder_division:
            print('True')
        else:
            print('False')
