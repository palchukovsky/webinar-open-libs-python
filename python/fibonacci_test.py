
import fibonacci


def test_calc_small():
    assert 55 == fibonacci.calc(10)
    assert 6765 == fibonacci.calc(20)


def test_calc_small_external():
    assert 55 == fibonacci.calc_externally(10)
    assert 6765 == fibonacci.calc_externally(20)


# def test_calc_big():
#    assert 1134903170 == fibonacci.calc(45)


def test_calc_big_externally():
    assert 1134903170 == fibonacci.calc_externally(45)


def test_series():
    expected = [0, 5, 55]

    calc = fibonacci.SeriesCalculator()

    calc.put_index(0)
    calc.put_index(5)
    calc.put_index(10)

    assert expected == calc.calc()


def test_series_externally():
    expected = [0, 5, 55]

    calc = fibonacci.ExternalSeriesCalculator()

    calc.put_index(0)
    calc.put_index(5)
    calc.put_index(10)

    assert expected == list(calc.calc())
