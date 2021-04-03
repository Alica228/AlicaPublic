import pytest

def ids_a(val):
    return "x=({0})".format(str(val))


def ids_b(val):
    return "y=({0})".format(str(val))


def ids_c(val):
    return "y=({0})".format(str(val))


@pytest.mark.parametrize("a", [-1, 0, 1, 2, 3], ids=ids_a)
@pytest.mark.parametrize("b", [-1, 0, 1, 2, 3], ids=ids_b)
@pytest.mark.parametrize("c", [-1, 0, 1, 2, 3], ids=ids_c)
def test_multiply_params(a, b, c):
    assert all([a+b > c, a+c > b, b+c > a]) == is_triangle(a, b, c)


def is_triangle(a, b, c):
    return True if a+b > c and a+c > b and b+c > a else False
