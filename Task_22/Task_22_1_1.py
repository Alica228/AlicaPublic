import pytest


def python_string_slicer(string):
    if len(string) < 50 or "python" in string:
        return string
    else:
        return string[0:50]


def generate_id(val):
    return "params: {0}".format(str(val))


@pytest.fixture(scope="function", params=[
   ("Короткая строка", "Короткая строка"),
   ("Длинная строка, не то чтобы прям очень длинная, но достаточно для нашего теста, и в ней нет названия языка"
    , "Длинная строка, не то чтобы прям очень длинная, но"),
   ("Короткая строка со словом python", "Короткая строка со словом python"),
   ("Длинная строка, нам достаточно будет для проверки, и в ней есть слово python"
    , "Длинная строка, нам достаточно будет для проверки, и в ней есть слово python"),
], ids=generate_id)
def param_fun_generated(request):
    return request.param


def test_python_string_slicer_generated(param_fun_generated):
    (input, expected_output) = param_fun_generated
    result = python_string_slicer(input)
    print("Входная строка: {0}\nВыходная строка: {1}\nОжидаемое значение: {2}".format(input, result, expected_output))
    assert result == expected_output
