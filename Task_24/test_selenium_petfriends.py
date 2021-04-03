import time


def test_petfriends(selenium):
	# Open PetFriends base page:
	selenium.get("https://petfriends1.herokuapp.com/")

	time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

	# click on the new user button
	btn_newuser = selenium.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")

	btn_newuser.click()

	# click existing user button
	btn_exist_acc = selenium.find_element_by_link_text(u"У меня уже есть аккаунт")
	btn_exist_acc.click()

	# add email
	field_email = selenium.find_element_by_id("email")
	field_email.clear()
	field_email.send_keys("<your_email>")

	# add password
	field_pass = selenium.find_element_by_id("pass")
	field_pass.clear()
	field_pass.send_keys("<your_password>")

	# click submit button
	btn_submit = selenium.find_element_by_xpath("//button[@type='submit']")
	btn_submit.click()

	time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!
	if selenium.current_url == 'https://petfriends1.herokuapp.com/all_pets':
		# Make the screenshot of browser window:
		selenium.save_screenshot('result_petfriends.png')
	else:
		raise Exception("login error")