'''
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
text = "Тест"
result = foo(text)
print(result)


S = ''
So = ''

def foo(S, So):
    return S.count(So)

result = foo(S, So)

print(result)
'''

a = [10, -5, 30, 25]

# 1. Сумм. полож 
sP = sum(x for x in a if x > 0)
print("1 задание:", sP)

maxE = max(a)

m1 = [x for x in a if maxE * 0.8 <= x <= maxE * 1.2]
m2 = [x for x in a if not (maxE * 0.8 <= x <= maxE * 1.2)]
result = m1 + m2

print("2 задание:", result)
