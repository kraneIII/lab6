'''
# Номер 1

import random

# Ввод количества строк и столбцов
M = int(input("Введите количество столбцов (M): "))
N = int(input("Введите количество строк (N): "))

mat = [[random.randint(1, 20) for _ in range(M)] for _ in range(N)]

# Выводим матрицу
print("Сгенерированная матрица:")
for row in mat:
    print(row)


# Найти минимальный элемент ниже побочной диагонали
if M == N:  
    minimum = float('inf')
    for i in range(1, N):
        for j in range(N - i, N):
            if mat[i][j] < minimum:
                minimum = mat[i][j]

    print(f"Минимальный элемент ниже побочной диагонали: {minimum}")
else:
    print("Матрица не квадратная, вычисление невозможно.")
'''
'''
# Номер 2

N = int(input("Введите порядок квадратной матрицы (N): "))

mat = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            at[i][j] = n- I
        elif j < i:
            mat[i][j] = i - j
        elif j > i:
            mat[i][j] = 0
print("Квадратный список:)
for row in mat:
      print(row)
'''
# Номер 3

import random

# Ввод строки пользователем
stri = input("Введите строку (или нажмите Enter для генерации случайной): ")
if not stri:
    stri = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(20))

# Создание словаря
counter = {}
for char in stri:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':  # Проверка, что символ - буква
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

# Вывод строки и словаря
print(f"Использованная строка: {stri}")
print("Словарь букв и их частоты:")
for key, value in counter.items():
    print(f"'{key}': {value}")

# Поиск буквы
searcher = input("Введите букву для поиска: ")
if searcher in counter:
    print("Буква '{searcher}' встречается {counter[searcher]}

      
