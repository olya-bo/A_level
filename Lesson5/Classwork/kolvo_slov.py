with open('text.txt','r') as text:
    text = ''.join(text.readlines()).split()

all_word = set(text)

ans_1 = dict(map(lambda x: (x, text.count(x)), all_word))

list(map(lambda x: print(f'{x[0]} - {x[1]}'), ans_1.items()))

# a = [[10, 20], [30, 40], [50, 60]]
# list(map(lambda val: list(map(print, val)), a))
