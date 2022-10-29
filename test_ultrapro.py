'''
В модуле написать тесты для встроенных функций filter, map, sorted, а также для
функций из библиотеки math: pi, sqrt, pow, hypot. Чем больше тестов на каждую
функцию - тем лучше
'''

import random
import math
import divisor_master
import functools

def test_filter():
    # test filter()
    lst = [1,1,2,5,4,6,8,0,5,2,1,3,6,9,8,7]
    assert list(filter(lambda x : x % 2==0, lst)) == [2,4,6,8,0,2,6,8]
    assert list(filter(lambda x : x<=0, lst)) == [0]
    assert len(list(filter(lambda x: x == 1, lst))) == 3
    assert len(list(filter(None, lst))) == len(lst)-lst.count(0)
    assert len(list(filter(divisor_master.itissimple, lst))) == 9

def test_map():
    # test map()
    def point_on_line(x,y,a,b):
        '''
        :param x, y: coordinates of point
        :param a, b: coefficients of line function y=a*x+b
        :return:  equals or not
        '''
        return y==a*x+b

    def less5(x):
        return x<5

    lst = [1, 1, 2, 5, 4, 6, 8, 0, 5, 2, 1, 3, 6, 9, 8, 7]
    # проверяется равенство ф-ии map и генератора списка с помощью ф-ии
    assert list(map(less5, lst)) == [less5(x) for x in lst]

    stepen = [2,3,4,5]
    # тест map работающей по двум спискам
    assert list(map(pow,lst,stepen)) == [1**2, 1**3, 2**4, 5**5]

    # тест map без преобразования в список , а как итератор
    lst_mapped = map(less5, lst)
    lst_index_less5 = []
    iCount=0
    while True:
        try:
            mapped_item = next(lst_mapped)
        except StopIteration:
            break
        if mapped_item:
            lst_index_less5.append(iCount)

        iCount+=1
    assert lst_index_less5 == [0, 1, 2, 4, 7, 9, 10, 11]

    # тест map на 4 списках
    lst_x = [1,2,3]
    lst_y = [4,8,6]
    lst_a = [2,3,2]
    lst_b = [2,2,1]

    assert list(map(point_on_line, lst_x, lst_y, lst_a, lst_b))[0]
    assert list(map(point_on_line, lst_x, lst_y, lst_a, lst_b))[1]
    assert not list(map(point_on_line, lst_x, lst_y, lst_a, lst_b))[2]


def test_sorted():
    #  test sorted
    dct_name = {1:'one',
                2:'two',
                3:'three',
                4:'four',
                5:'five',
                6:'six',
                7:'seven',
                8:'eight',
                9:'nine',
                0:'null'}

    lst = [1, 1, 2, 5, 4, 6, 8, 0, 5, 2, 1, 3, 6, 9, 8, 7]
    # sort by value
    assert sorted(lst) == [0, 1,1,1,2,2,3,4,5,5,6,6,7,8,8,9]
    # sort by name
    assert sorted(lst, key=(lambda x: dct_name[x])) == [8,8,5,5,4,9,0,1,1,1,7,6,6,3,2,2]

    assert sorted([9,3,1,7,5],reverse=True) == [9,7,5,3,1]

def test_pi():
    PI = math.pi
    assert round(PI,4) == 3.1416
    assert round(math.cos(PI/4),4) == round(math.sqrt(2) / 2 ,4)

def test_sqrt():
    assert math.sqrt(9) == 3
    assert math.sqrt(3**2+4**2) == 5
    SQ = math.sqrt
    assert SQ(625) == 25

def test_pow():
    POW = math.pow
    assert math.sqrt(POW(-3,2)+POW(4,2)) == 5
    assert POW(81,0.5) == math.sqrt(81)
    assert POW(10,-2) == 0.01

def test_hypot():
    # test hypotenuse in 1, 2 and 3 dimensional space with rounded result
    assert round(math.hypot(2),8) == round(math.sqrt(2 ** 2 ),8)
    assert round(math.hypot(2,3),8) == round(math.sqrt(2**2+3**2),8)
    assert round(math.hypot(2, 3, 7),8) == round(math.sqrt(2 ** 2 + 3 ** 2 + 7 ** 2),8)


    hypot = lambda a,b: math.sqrt(a**2+b**2)
    lst=[3,5,6,3,8,5,0]
    assert functools.reduce(hypot, lst) == math.hypot(*lst)


