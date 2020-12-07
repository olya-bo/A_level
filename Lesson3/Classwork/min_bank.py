kypur_keys = (10, 20, 50, 100, 200, 500, 1000)
kypurs = {
    10: 0,
    20: 0,
    50: 0,
    100: 0,
    200: 0,
    500: 0,
    1000: 0,
}
kypur_index = 0

money_input = int(input('Enter the sum multiple of 10 and and less than 18800: '))

while money_input % 10 != 0 or money_input > 18801:
    print('Sory, try again')
    money_input = int(input('Enter the sum multiple of 10 and less than 18800: '))

while True:
    kypur = kypur_keys[kypur_index]
    if money_input % kypur == 0:
        for _ in range(10 - kypurs[kypur]):
            money_input -= kypur
            kypurs[kypur] += 1
            if money_input == 0:
                break
        else:
            kypur_index += 1
            continue
    else:
        money_input += kypur_keys[kypur_index - 1]
        kypurs[kypur_keys[kypur_index- 1]] -= 1
        continue
    break

for kypur in kypurs:
    if kypurs[kypur] > 0:
        print(f'{kypur} - {kypurs[kypur]}')
