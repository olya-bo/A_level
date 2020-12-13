text1 =  '''One advanced diverted domestic sex repeated bringing you old.
Possible procured her trifling laughter thoughts property she met way.
Companions shy had solicitude favourable own. Which could saw guest man now heard but.
Lasted my coming uneasy marked so should.
Wooded ladies she basket season age her uneasy saw.
Discourse unwilling am no described dejection incommode no listening of.
Before nature his parish boy. '''.split('\n')

text2 = '''Oneee advanced diverted domestic sex repeated bringing you old.
Possible procured her trifling laughter thoughts property she met way.
Which could saw guest man now heard but.
Lasted my coming uneasy marked so should. Gravity letters it amongst herself dearest an windows by.
Wooded ladies she basket season age her uneasy saw. 
Discourse unwilling am no described dejection incommode no listening of. '''.split('\n')

def array_difference(array1, array2):
    ans = 0
    for word1, word2 in zip(array1, array2):
        new_ans = abs(len(word1) - len(word2))
        if new_ans > ans:
            ans = new_ans
    return ans

number = array_difference(text1, text2)
print(f'The biggest difference is in the array - {number}')
