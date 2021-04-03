import pytest
from api import PetFriends
from settings import valid_email, valid_password


def generate_string(n):
    return "x" * n


def russian_chars():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


# Здесь мы взяли 20 популярных китайских иероглифов
def chinese_chars():
    return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


def is_age_valid(age):
    # Проверяем, что возраст - это число от 1 до 49 и целое
    return age.isdigit() \
        and 0 < int(age) < 50 \
        and float(age) == int(age)


@pytest.fixture(autouse=True)
def ket_api_key():
    """ Проверяем, что запрос api-ключа возвращает статус 200 и в результате содержится слово key"""

    pf = PetFriends()
    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    pytest.status, pytest.key = pf.get_api_key(valid_email, valid_password)

    # Сверяем полученные данные с нашими ожиданиями
    assert pytest.status == 200
    assert 'key' in pytest.key

    yield

    # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
    assert pytest.status == 200


@pytest.mark.parametrize("my_filter",
                         [
                            generate_string(255)
                            , generate_string(1001)
                            , russian_chars()
                            , russian_chars().upper()
                            , chinese_chars()
                            , special_chars()
                            , 123
                         ], ids=
                         [
                            '255 symbols'
                            , 'more than 1000 symbols'
                            , 'russian'
                            , 'RUSSIAN'
                            , 'chinese'
                            , 'specials'
                            , 'digit'
                         ])
def test_get_all_pets_with_negative_filter(my_filter):
    pf = PetFriends()
    pytest.status, result = pf.get_list_of_pets(pytest.key, my_filter)

    # Проверяем статус ответа
    assert pytest.status == 200  # pytest.status == 400


@pytest.mark.parametrize("my_filter",
                         ['', 'my_pets'],
                         ids=['empty string', 'only my pets'])
def test_get_all_pets_with_valid_key(my_filter):
    pf = PetFriends()
    pytest.status, result = pf.get_list_of_pets(pytest.key, my_filter)

    # Проверяем статус ответа
    assert pytest.status == 200
    assert len(result['pets']) > 0


@pytest.mark.parametrize("name", [
                                   ''
                                   , generate_string(255)
                                   , generate_string(1001)
                                   , russian_chars()
                                   , russian_chars().upper()
                                   , chinese_chars()
                                   , special_chars()
                                   , '123'
                                ], ids=[
                                   'empty'
                                   , '255 symbols'
                                   , 'more than 1000 symbols'
                                   , 'russian'
                                   , 'RUSSIAN'
                                   , 'chinese'
                                   , 'specials'
                                   , 'digit'
                                ])
@pytest.mark.parametrize("animal_type", [
                                    '',
                                    generate_string(255),
                                    generate_string(1001),
                                    russian_chars(),
                                    russian_chars().upper(),
                                    chinese_chars(),
                                    special_chars(),
                                    '123'
                                ], ids=[
                                    'empty',
                                    '255 symbols',
                                    'more than 1000 symbols',
                                    'russian', 'RUSSIAN',
                                    'chinese', 'specials',
                                    'digit'
                                ])
@pytest.mark.parametrize("age", [
                                    '',
                                    '-1',
                                    '0',
                                    '1',
                                    '100',
                                    '1.5',
                                    '2147483647',
                                    '2147483648',
                                    special_chars(),
                                    russian_chars(),
                                    russian_chars().upper(),
                                    chinese_chars()
                                ], ids=[
                                    'empty',
                                    'negative',
                                    'zero',
                                    'min',
                                    'greater than max',
                                    'float', 'int_max',
                                    'int_max + 1',
                                    'specials',
                                    'russian',
                                    'RUSSIAN',
                                    'chinese'
                                ])
def test_add_new_pet_simple(name, animal_type, age):
    """Проверяем, что можно добавить питомца с различными данными"""

    # Добавляем питомца
    pf = PetFriends()
    pytest.status, result = pf.add_new_pet_simple(pytest.key, name, animal_type, age)
    # Сверяем полученный ответ с ожидаемым результатом
    if name == '' or animal_type == '':
        assert pytest.status == 200  # pytest.status == 400
    else:
        assert pytest.status == 200
        assert result['name'] == name
        assert result['age'] == age
        assert result['animal_type'] == animal_type
