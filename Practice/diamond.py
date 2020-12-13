number = int(input('Put your number '))
symbol = '*'
ans = []
if number > 0 and number % 2 != 0:
    count = number // 2
    for i in range((number // 2) + 1):

        symbols = ' ' * count + symbol
        ans.append(symbols)
        symbol += '*' * 2
        count -= 1
for i in ans:
    print(i)
for j in reversed(ans[:-1]):
    print(j)
