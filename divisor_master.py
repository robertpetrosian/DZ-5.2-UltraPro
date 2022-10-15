# global LST_SIMPLE  # глобальная переменная список простых чисел
LST_SIMPLE = []

def get_simple(N=10000):
    '''
    ф-я получения списка простых чисел от 1 до N
    :param N: до какого числа выбирать простые числа
    :return: список простых чисел
    '''
    lst=[x for x in range(2,N+1)] #список всех чисел от 2 о 1000
    rez=[1] # первый элемент списка
    while len(lst) > 0:
        # пока есть элементы в исходном списке чисел
        rez.append(lst.pop(0)) # перенести первый элемент в список простых чисел
        # оставить  числа некратные последнему простому числу
        lst = list(filter((lambda x: x % rez[-1] != 0), lst))

    return sorted(rez)

# ф-я проверки числа на простоту
# возвращает истину если число входит в список простых чисел
itissimple = (lambda x: x in LST_SIMPLE)

# ф-я список делителей
# получает x возвращает список созданный фильтром кратности
# элементов списка простых чисел
def lst_dividers(x):
    rez = list(filter(lambda y: x % y ==0, LST_SIMPLE))
    return rez

# ф-я возвращает максимальный делитель числа.
max_divider = lambda x: lst_dividers(x)[-1]

def factorize(x):
    '''
    # функция выводит каноническое разложение числа на простые множители
    :param x: число
    :return: список множителей
    '''
    lst = []
    # ф-я получения след делителя , кроме 1
    next_divider = lambda x, z: list(filter(lambda y: x % y == 0, z))[0]

    while x>1:
        n = next_divider(x, lst_dividers(x)[1:])
        x //= n
        lst.append(n)
    lst.insert(0, 1)
    return sorted(lst)

LST_SIMPLE = get_simple()
