import functions as fn

def test_F():
    assert len(fn.F(['abs','abv','cdf'],12)) == 12
    assert len(fn.F([],2)) == 0
    assert fn.Often(['abs','abv','cdf','abs','cdf','abs','abv']) == 'abs'
    assert fn.Often([1,'abv','cdf',1,'cdf',1,'abv']) == 1
    assert fn.Rarely(['abs','abv','cdf','abs','cdf','abs','abv']) == 'c'

