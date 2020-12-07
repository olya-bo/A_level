def kvadrat_sum(number):
    delitel = 0
    for i in range(1, number+1):
        if number % i == 0:
            delitel += 1
            if delitel > 2:
                break
    else:
        return number**2
    return number


# a = kvadrat_sum(int(input('Put some number ')))
# print(a)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_numbers = list(map(kvadrat_sum, numbers))
print(squared_numbers)