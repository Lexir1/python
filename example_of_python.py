print('Hello world')  # изучил комментарий,долго не понимал что надо два пробела
'''Это многострочная строка. Это её первая строка
Это её вторая строка.
"Как ваше имя?",- спросил я.
Он ответил"Бонд,Джеймс Бонд."'''  # изучил тройные кавычки

import math
def f():
    '''
    Super-puper function f

    The function doing nothing :)
    '''


print(f.__doc__)
print(math.__doc__)
age = 57
name = "Peso"
print('Возраст {0} -- {1} лет'.format(name,age))
print("Почему{0} забавляется с этим Python?".format(name))
