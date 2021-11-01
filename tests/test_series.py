 
from math_series.series import sum_series

def test_sum_fibonacci_5():
    expected = 7
    actual = sum_series(5)
    assert expected == actual

def test_sum_fibonacci_6():
    expected = 12
    actual = sum_series(6,0,1)
    assert expected == actual

def test_lucas_4():
    expected = 10
    actual = sum_series(4,2,1)
    assert expected == actual

def test_lucas_5():
    expected = 17
    actual = sum_series(5,2,1)
    assert expected == actual