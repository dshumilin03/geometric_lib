import pytest

import calculate

test_data = [
    ("circle", "area", [5]),
    ("circle", "perimeter", [5]),
    ("square", "area", [4]),
    ("square", "perimeter", [4])
]


@pytest.mark.parametrize("fig, func, size", test_data)
def test_calc_successor(fig, func, size):
    # given

    # when
    result = calculate.calc(fig, func, size)

    # then
    assert isinstance(result, (int, float))


def test_calc_invalid_figure():
    # given
    fig = 'invalid-figure'
    func = 'area'
    size = [3]

    # when and then
    with pytest.raises(AssertionError):
        calculate.calc(fig, func, size)


def test_calc_invalid_function():
    # given
    fig = 'square'
    func = 'invalid-function'
    size = [3]

    # when and then
    with pytest.raises(AssertionError):
        calculate.calc(fig, func, size)


def test_calc_invalid_size():
    # given

    fig = 'square'
    func = 'area'
    size = ["wrong"]

    # when and then
    with pytest.raises(TypeError):
        calculate.calc(fig, func, size)


def test_calc_invalid_size_key():
    # given
    fig = 'square'
    func = 'area'
    size = [1, 2]

    # when and then
    with pytest.raises(TypeError):
        calculate.calc(fig, func, size)
