# class Car:
#     color = 'red'
#     top_speed = 250
#
# zaz = Car()
# toyta = Car()
#
# zaz.top_speed = 40
#
# print(toyta.color, toyta.top_speed)
# print(zaz.color, zaz.top_speed)
#
# def eggs():
#     print('Hello')
#
# def spam(somefoo):
#     print(somefoo())
#
# spam(eggs)

# class SmartPhone:
#     brand = ''
#     price = 0
#
#
#     def call(self, name):
#         return '{} ring ring to {}'.format(self.brand, name)
#
#     def print_self(self):
#         return self.__class__
#
# samsung = SmartPhone()
# samsung.brand = 'samsung'
# samsung.price = 500
#
# xiaomi = SmartPhone()
# xiaomi.brand = 'xiaomi'
# xiaomi.price = 100
#
# print(xiaomi.print_self())
# print(samsung.call('Olha'))


#task1

# class SmartPhone:
#     brand = ''
#     price = 0
#
#     phone_book = {'dima': ''}
#
#     def call(self, name):
#         self.shutdown()
#         return 'Call to {}'.format(self.phone_book[name])
#
#     def shutdown (self):
#         print('shutdown !!!!111100000!!!!')
#
# siemens = SmartPhone()
# siemens.brand = 'siemens'
# siemens.price = 50
# siemens.phone_book = {'pol': '88005553535', 'halom' : '9379992'}
#
# #print(siemens.call('pol'))
#
# iphone = SmartPhone()
# iphone.brand = 'apple'
# iphone.price = 1300
# iphone.phone_book = {'steve': '+1 777 888', 'tim': '+1 999 000'}
#
# print(iphone.call('steve'))

#task3

class SmartPhone(object):
    brand = ''
    price = 0

    phone_book = {'dima': ''}

    def call(self, name):
        return 'Call to {}'.format(self.phone_book[name])

class Phone(SmartPhone):
    def call(self, number):
        return f'Ring ring to {number}'

iphone = SmartPhone()
iphone.brand = 'apple'

electronica = Phone()
electronica.brand = 'ussr'

print(electronica.call(206947))