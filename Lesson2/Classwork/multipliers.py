digital = int(input())
x = len(str(digital)) - 1
digital_sotni = []
for i in range(len(str(digital))):
    print(f'{str(digital)[i]} * 10^{x}', end='')
    if x > 0:
        print(' +', end=' ')
        digital_sotni.append(int(str(digital)[i]) * 10 ** x)
    else:
        print()
        digital_sotni.append(int(str(digital)[i]) * 10 ** x)
        pass
    x -= 1

def mnoz(i):
    ans = []
    b = 2
    while i > 1:
        if i % b == 0:
            ans.append(b)
            i /= b
        else:
            b += 1
    return ans

for i in digital_sotni:
    print(f'Mножители числа {i} =', ' * '.join([str(x) for x in mnoz(i)]))