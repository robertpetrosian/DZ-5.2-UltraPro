import divisor_master as dm

def test_get_simple():
    assert dm.get_simple(20) == [1,2,3,5,7,11,13,17,19]
    assert dm.get_simple(-20) == [1]
    assert dm.get_simple(-3) == [1]

def test_itissimple():
    assert dm.itissimple(13) == True
    assert dm.itissimple(130) == False
    assert dm.itissimple(0) == False

def test_lst_dividers():
    assert dm.lst_dividers(100) == [1,2,5]
    assert dm.lst_dividers(0) == [1]
    assert dm.lst_dividers(-5) == [1]
    assert dm.lst_dividers(13) == [1, 13]
    assert dm.lst_dividers(13.99) == [1, 13]
    assert dm.lst_dividers(1.3) == [1]

def test_max_divider():
    assert dm.max_divider(100) == 5
    assert dm.max_divider(0) == 1
    assert dm.max_divider(-5) == 1
    assert dm.max_divider(13) == 13
    assert dm.max_divider(13.99) == 13
    assert dm.max_divider(1.3) == 1



