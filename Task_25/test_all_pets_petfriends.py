import pytest
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
		EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.card img.card-img-top'))
	)

	yield

	pytest.driver.quit()


def test_all_pets():
	images = pytest.driver.find_elements_by_css_selector('div.card img.card-img-top')
	names = pytest.driver.find_elements_by_css_selector('div.card h5.card-title')
	descriptions = pytest.driver.find_elements_by_css_selector('div.card p.card-text')

	for i in range(len(names)):
		assert images[i].get_attribute('src') != ''
		assert names[i].text != ''
		assert descriptions[i].text != ''
		assert ', ' in descriptions[i].text
		parts = descriptions[i].text.split(", ")
		assert len(parts[0]) > 0
		assert len(parts[1]) > 0
