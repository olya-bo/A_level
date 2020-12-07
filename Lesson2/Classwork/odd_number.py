digital = int(input('Please, put you number '))
if digital % 2 != 0:
    if digital % 3 == 0 and digital % 5 == 0 and digital % 10 != 0:
        print(f"{digital} number fits")
    else:
        print(f"{digital} doesn't fit")
else:
    print(f"{digital} doesn't fit")