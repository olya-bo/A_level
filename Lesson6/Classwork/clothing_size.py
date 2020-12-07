international_size = {'xxs': {'Russua': 42, 'German': 36, 'USA': 8, 'France': 38, 'United Kingdom': 24},
                      'xs': {'Russua': 44, 'German': 38, 'USA': 10, 'France': 40, 'United Kingdom': 26},
                      's': {'Russua': 46, 'German': 40, 'USA': 12, 'France': 42, 'United Kingdom': 28},
                      'm': {'Russua': 48, 'German': 42, 'USA': 14, 'France': 44, 'United Kingdom': 30},
                      'l': {'Russua': 50, 'German': 44, 'USA': 16, 'France': 46, 'United Kingdom': 32},
                      'xl': {'Russua': 52, 'German': 46, 'USA': 18, 'France': 48, 'United Kingdom': 34},
                      'xxl': {'Russua': 54, 'German': 48, 'USA': 20, 'France': 50, 'United Kingdom': 36},
                      'xxxl': {'Russua': 56, 'German': 50, 'USA': 22, 'France': 52, 'United Kingdom': 38},
                      }

def universal_in_other(size):
    if size in international_size:
        return international_size[size]
    else:
        return {}

def main():
    while True:
        input_size = input('Put your size ').lower()
        ans = universal_in_other(input_size)
        if ans:
            for key, value in ans.items():
                print(f'{key} - {value}')
            break
        else:
            print("Sorry, but we don't have this size")
            print('Try again')
main()
