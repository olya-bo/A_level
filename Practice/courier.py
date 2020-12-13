floor = int(input('Floor of house ' ))
apartments_on_floor = int(input('Appartments on floor '))
apartment = int(input("Input your apartment "))
entrance = 0
apartment_entrance = apartment

while True:
    if apartment_entrance > floor * apartments_on_floor:

        apartment_entrance -= (floor * apartments_on_floor)
        entrance += 1
        continue
    else:
        entrance += 1
        if (floor * apartments_on_floor) - apartment_entrance > 0:

            floor_home = (apartment_entrance // 4) + 1
        else:
            floor_home = floor
        break

print(f'Entrance {entrance} - floor {floor_home}')