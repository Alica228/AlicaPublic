import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def testing():
	pytest.driver = webdriver.Chrome('../chromedriver.exe')
	# Переходим на страницу авторизации
	pytest.driver.get('http://petfriends1.herokuapp.com/login')

	yield

	pytest.driver.quit()


def test_show_my_pets():
	# Вводим email
	pytest.driver.find_element_by_id('email').send_keys('vasya@mail.com')
	# Вводим пароль
	pytest.driver.find_element_by_id('pass').send_keys('12345')
	# Нажимаем на кнопку входа в аккаунт
	pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
	# Проверяем, что мы оказались на главной странице пользователя
	assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
