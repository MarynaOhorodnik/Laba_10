'''
Сформувати функцію, що визначатиме чи є задане натуральне число простим.
Простим називається число, що більше за 1 та не має інших дільників, окрім 1 та самого себе).
Огороднік Марина Олександрівна, І курс, група 122А
'''
'''
У даному випадку доцільніше використовувати функцію з ітерацією; час розробки трохи менший у випадку з ітерацією;
читабельність краща у випадку з рекурсією; час виконання функцій менщий у випадку з ітерацією;
пам'ять (стек) у випадку з рекурсіює використовується не доцільно, тому що результат кожного виклику вноситься у стек,
а ці дані не є важливими (потрібними)
'''
import timeit  # імпортуємо модуль для обрахунку часу роботи функцій
def func_rec(x, k = 2):
    ''' Функція для визначення чи є задане число простим за допомогою рекурсії

    :param x: вихідне число
    :param k: змінна для визначення дільника (за замовч. починається з 2)
    :return: змінна res (True або False)
    '''
    result = True  # вводимо змінну щоб визначити результат чи є чило простим (припускаємо, що число є простим)
    if x > 1:  # перевірка чи число більше 1, бо усі проті числа більше одиниці
        if k < x:  # рекурсія буде продовжуватися, поки дільник не буде дорівнювати вихідному числу
            if x % k != 0:  # якщо не знайдено дільник, то продовжується пошук
                k += 1  # збільшуємо значення дільника на одиницю
                func_rec(x, k)
            else:   # якщо знайдено хоча б один дільник, то функція завершує роботу, тому що число точно не є простим
                result = False
                return result
    else:
        return False
    return result

def func_iter(y):
    ''' Функція для визначення чи є задане число простим за допомогою ітерації

    :param y: вихідне число
    :return: результат True або False
    '''
    if y > 1:  # перевірка чи число більше 1, бо усі проті числа більше одиниці
        result = True  # вводимо змінну, яка визначатиме, чи є задане число простим
# доцільно перевіряти числа, як закінчуються на 1, 3, 7, 9, бо числа, які закінчуються на 2, 5, 0 точно не є простими
        if y % 10 in [1, 3, 7, 9]:
            for i in range(2, y):  # циклічно перевіряємо усі дільники окрім 1 та самого числа
                if y % i == 0:  # якщо знайдено хоча б один дільник, то доцільно завершити цикл, бо число не є простим
                    result = False
                    break
        else:
            result = False
        return result
    else:
        return False

while True:
    while True:
        try:  # перевірка на правильність введення даних
            A = int(input('Input a number: '))
            if A > 0:   # виключення випадку, що користувач введе число менше 0
                break
        except ValueError:
            print('It is not a number')
    # виводимо результат і час виконання функції
    print(f'Recursion: \nPrime number = {func_rec(A)}, '
          f'\ntime = {timeit.timeit("func_rec(A)", setup="from __main__ import func_rec, A", number=1000)}')
    print(f'Iteration: \nPrime number = {func_iter(A)}, '
          f'\ntime = {timeit.timeit("func_iter(A)", setup="from __main__ import func_iter, A", number=1000)}')

    # запитуємо кристувача чи продовжувати роботу далі, чи завершити програму
    answer = input('Do you want to continue (+) or complete the program (anything)? ')
    if answer == '+':
        continue
    else:
        break