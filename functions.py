import random

def F(lst,N=10):
    '''
    ф-я возвращает список N произвольных элементов из списка lst
    :param lst:входящий список
    :param N: количество элементов выходного списка (по умолчанию 10)
    :return: список N случайных элементов из lst
    '''

    if len(lst) ==0 or N <= 0: return []

    lst_indexes = [random.randint(0,len(lst)-1) for x in range(N)] # список индексов lst длиной N

    return list(map(lambda x: lst[x] , lst_indexes))

def Often(lst):
    '''
    ф-я выводит наиболее часто встречаемый элемент списка
    :param lst: список
    :return: эдемент
    '''

    if len(lst) ==0 : return ''

    lst_tmp = list(set(lst)) # список уникальных имен
    dct_tmp = dict([(x,lst.count(x)) for x in lst_tmp ]) # словарь (имя, счетчик)
    lst_tmp_sort = sorted(dct_tmp,key=dct_tmp.get, reverse=True) # сортировка словаря
    return lst_tmp_sort[0]

def Rarely(lst):
    '''
    ф-я вывода самой редкой первой буквы

    :param lst: список имен
    :return: имя с самой редкой буквы

    '''

    if len(lst) == 0 : return ''

    lst_tmp = list(set([x[0] for x in lst])) # список уникальных первых букв
    dct_tmp = dict([(x,len(list(filter(lambda y: y[0]==x, lst))))  for x in lst_tmp ]) # словарь (первая буква имени, счетчик)
    lst_tmp_sort = sorted(dct_tmp,key=dct_tmp.get)

    return lst_tmp_sort[0]
