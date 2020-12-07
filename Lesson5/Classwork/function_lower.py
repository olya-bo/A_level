def text_lower(text):
    return text.lower()

def text_upper(text):
    return text.upper()


text = ['Hello', 'my', 'name', 'is', 'Olya']
squared_numbers_1 = list(map(text_lower, text))
squared_numbers_2 = list(map(text_upper, text))
print(squared_numbers_1)
print(squared_numbers_2)