'''
#Номер 1
def foo(text):
    # Разбиваем
    words = text.split()
    
    # Обрабатываем каждое слово по отдельности
    wordsArray = []
    for word in words:
        if len(word) > 1:
            w = word[-1] + word[:-1]
        else:
            w = word
        wordsArray.append(w)

        return ' '.join(wordsArray)

#Использование функции
text = input('Add text to change')
result = foo(text)
print(result)

'''
#Номер 2
S = input('Enter word where u want to find')
So = input('Enter word to find')

def foo(S, So):
    return S.count(So)

result = foo(S, So)

print(result)

from random import randint
'''
#Номер 3
a = []
for x in range(1, 10):
    a.append(randint(-100, 100))
print(a, '- original array' )

# 1. Сумм. полож
try:
    sP = sum(x for x in a if x > 0)
    print("1 task:", sP)

    maxE = max(a)

    m1 = [x for x in a if maxE * 0.8 <= x <= maxE * 1.2]
    m2 = [x for x in a if not (maxE * 0.8 <= x <= maxE * 1.2)]
    result = m1 + m2
except:
    print('Wrong entered data')

print("2 task:", result)
'''
