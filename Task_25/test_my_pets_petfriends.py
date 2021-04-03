import pytest
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
	pytest.driver = webdriver.Chrome('../chromedriver.exe')
	pytest.driver.implicitly_wait(10)
	# Переходим на страницу авторизации
	pytest.driver.get('http://petfriends1.herokuapp.com/login')
	pytest.driver.find_element_by_id('email').send_keys('e4syway@yandex.rus')
	pytest.driver.find_element_by_id('pass').send_keys('123')
	pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
	# Переходим на страницу с моими питомцами
	element = WebDriverWait(pytest.driver, 10).until(
		EC.visibility_of_element_located((By.CSS_SELECTOR, "a.nav-link[href='/my_pets']"))
	)
	element.click()
	_ = WebDriverWait(pytest.driver, 10).until(
		EC.visibility_of_element_located((By.CSS_SELECTOR, 'table.table.table-hover > tbody > tr'))
	)

	yield

	pytest.driver.quit()


def test_number_of_pets():
	table = pytest.driver.find_elements_by_css_selector('table.table.table-hover > tbody > tr')
	number_of_pets = pytest.driver.find_element_by_css_selector('div.\.col-sm-4.left')
	number_of_pets = int(re.findall("Питомцев: (\d*)\n", number_of_pets.text)[0])
	assert number_of_pets == len(table), f"Количество питомцев не совпадает! Пишется в статистике: {number_of_pets}, количество карточек: {len(table)}"


def test_photo_of_pets():
	table = pytest.driver.find_elements_by_css_selector('table.table.table-hover > tbody > tr')
	all_images = [row.find_element_by_css_selector('th > img').get_attribute('src') for row in table]
	number_of_not_empty_images = len(list(filter(lambda x: x != '', all_images)))
	assert number_of_not_empty_images >= len(table) // 2


def test_name_animal_type_age_of_pets():
	table = pytest.driver.find_elements_by_css_selector('table.table.table-hover > tbody > tr')
	for row in table:
		name, animal_type, age, _ = row.find_elements_by_css_selector('td')
		assert '' not in [name.text, animal_type.text, age.text], f"Какое-то из значений пустое! name: {name.text}, animal_type: {animal_type.text}, age: {age.text}"


def test_all_names_of_pets_are_unique():
	table = pytest.driver.find_elements_by_css_selector('table.table.table-hover > tbody > tr')
	all_names = [row.find_elements_by_css_selector('td')[0].text for row in table]
	assert len(all_names) == len(set(all_names)), f"Не все имена уникальные! {all_names}"


def test_data_of_pets_are_unique():
	table = pytest.driver.find_elements_by_css_selector('table.table.table-hover > tbody > tr')
	all_data = []
	for data in [row.find_elements_by_css_selector('td')[0:-1] for row in table]:
		all_data += [tuple(map(lambda x: x.text, data))]
	assert len(all_data) == len(set(all_data)), f"Не все питомцы уникальные! {all_data}"
