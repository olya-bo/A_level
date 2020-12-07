money = (1000, 500, 200, 100, 50, 20, 10, 5, 2, 1)

money_input = int(input('Put money '))
ans = []
count = 0
while money_input > 0:
    if money_input - money[count] >= 0:
        ans.append(money[count])
        money_input -= money[count]
    else:
        count += 1


print()
# for i in money:
#     if i in ans:
#         print(f"{i} - {ans.count(i)}")
