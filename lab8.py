import random

# Функция для автоматического заполнения списка
def listRandom(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]

# Номер 1
def foo1():
    X = listRandom(15, -10, 10)
    Y = listRandom(20, -10, 10)
    print(f"Массив X: {X}")
    print(f"Массив Y: {Y}")
    a = min(X)
    b = min(Y)
    if a * b == 0:
        print("Ошибка: Нельзя делить на ноль!")
        return
    z = (a + b) / (a * b)
    print(f"Минимальный элемент X: {a}, Минимальный элемент Y: {b}")
    print(f"Результат z: {z}")
foo1()

# Номер 2
def foo():
    A = listRandom(15, -10, 10)
    B = listRandom(20, -10, 10)
    print(f"Массив A: {A}")
    print(f"Массив B: {B}")
    S1 = sum(x for x in A if x > 0)
    S2 = sum(x for x in B if x > 0)
    k1 = len([x for x in A if x > 0])
    k2 = len([x for x in B if x > 0])
    if S1 + S2 == 0:
        print("Ошибка: Деление на ноль!")
        return
    U = (k1**1.5 * k2**1.5) / (S1 + S2)
    print(f"Сумма положительных элементов A: {S1}, количество: {k1}")
    print(f"Сумма положительных элементов B: {S2}, количество: {k2}")
    print(f"Результат U: {U}")
foo()

# Задача 3: Рекурсивная функция degree5
def foo2(N):
    if N < 1:
        return -1
    if N == 1:
        return 0
    if N % 5 != 0:
        return -1
    return 1 + foo2(N // 5)

# Главная функция
def fooMain():
    while True:
        print("\nВыберите задачу:")
        print("1 - Вычислить z")
        print("2 - Вычислить U")
        print("3 - Определить степень числа 5")
        print("0 - Выйти")
        choice = input("Ваш выбор: ")
        
        if choice == "1":
            foo1()
        elif choice == "2":
            foo()
        elif choice == "3":
            try:
                N = int(input("Введите натуральное число N: "))
                result = foo2(N)
                print(f"Результат foo2({N}): {result}")
            except ValueError:
                print("Ошибка: Введите корректное число!")

        elif choice == "0":
            print("Выход из программы.")
    
            break
        else:
            print("Ошибка: Некорректный ввод!")

if fooMain == "__fooMain__":
    fooMain()

