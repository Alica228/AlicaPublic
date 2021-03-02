import pytest, os
from api import PetFriends
from settings import email, password


class TestPetFriends:
    def setup(self):
        self.pf = PetFriends()

    def test_successful_get_api_key_for_valid_user(self, email=email, password=password):
        status, result = self.pf.get_api_key(email, password)
        
        assert status == 200
        assert "key" in result

    def test_successful_get_all_pets_with_valid_key(self, email=email, password=password, filters=""):
        _, auth_key = self.pf.get_api_key(email, password)
        status, result = self.pf.get_list_of_pets(auth_key, filters)
        
        assert status == 200
        assert len(result["pets"]) > 0

    def test_successful_add_new_pet_with_valid_data(self, email=email, password=password, name='Барбоскин', animal_type='двортерьер', age='4', pet_photo='images/QAP_19.4.1.png'):
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
        _, auth_key = self.pf.get_api_key(email, password)
        status, result = self.pf.post_new_pet(auth_key, name, animal_type, age, pet_photo)
        
        assert status == 200
        assert len(result) > 0
        
    def test_wrong_add_new_pet_with_invalid_data_1(self, email=email, password=password, name='', animal_type='двортерьер', age='4', pet_photo='images/QAP_19.4.1.png'):
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
        _, auth_key = self.pf.get_api_key(email, password)
        status, result = self.pf.post_new_pet(auth_key, name, animal_type, age, pet_photo)
        
        assert status == 400, "Загрузил питомца с пустым name"

    def test_wrong_add_new_pet_with_invalid_data_2(self, email=email, password=password, name='Барбоскин', animal_type='', age='4', pet_photo='images/QAP_19.4.1.png'):
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
        _, auth_key = self.pf.get_api_key(email, password)
        status, result = self.pf.post_new_pet(auth_key, name, animal_type, age, pet_photo)
        
        assert status == 400, "Загрузил питомца с пустым animal_type"

    def test_wrong_add_new_pet_with_invalid_data_3(self, email=email, password=password, name='Барбоскин', animal_type='двортерьер', age='', pet_photo='images/QAP_19.4.1.png'):
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
        _, auth_key = self.pf.get_api_key(email, password)
        status, result = self.pf.post_new_pet(auth_key, name, animal_type, age, pet_photo)
        
        assert status == 400, "Загрузил питомца с пустым age"

    def test_wrong_add_new_pet_with_invalid_data_4(self, email=email, password=password, name='Барбоскин', animal_type='двортерьер', age='4', pet_photo='images/PetFriends_ My_Pets.html'):
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
        _, auth_key = self.pf.get_api_key(email, password)
        status, result = self.pf.post_new_pet(auth_key, name, animal_type, age, pet_photo)
        
        assert status == 400, "Загрузил вместо фотки html файл"

    def test_successful_delete_pet(self, email=email, password=password):
        _, auth_key = self.pf.get_api_key(email, password)
        _, result = self.pf.get_list_of_pets(auth_key, "my_pets")
        
        if len(result['pets']) > 0:
            pet_id = result['pets'][0]['id']
            status = self.pf.delete_pet(auth_key, pet_id)
            assert status == 200
        else:
            raise Exception("There is no my pets")

    def test_wrong_delete_pet_with_wrong_id(self, email=email, password=password):
        _, auth_key = self.pf.get_api_key(email, password)
        _, result = self.pf.get_list_of_pets(auth_key, "my_pets")
        
        if len(result['pets']) > 0:
            pet_id = result['pets'][0]['id'][::-1]
            status = self.pf.delete_pet(auth_key, pet_id)
            assert status == 400, "Удалил питомца с неверным pet_id"
        else:
            raise Exception("There is no my pets")

    def test_wrong_delete_pet_with_wrong_auth_key(self, email=email, password=password):
        _, auth_key = self.pf.get_api_key(email, password)
        _, result = self.pf.get_list_of_pets(auth_key, "my_pets")
        
        if len(result['pets']) > 0:
            pet_id = result['pets'][0]['id']
            auth_key["key"] = auth_key["key"][::-1]
            status = self.pf.delete_pet(auth_key, pet_id)
            assert status == 403
        else:
            raise Exception("There is no my pets")

    def test_successful_update_self_pet_info(self, email=email, password=password, name='Мурзик', animal_type='Котэ', age=5):
        _, auth_key = self.pf.get_api_key(email, password)
        _, result = self.pf.get_list_of_pets(auth_key, "my_pets")

        if len(result['pets']) > 0:
            pet_id = result['pets'][0]['id']
            status, result = self.pf.update_pet_info(auth_key, pet_id, name, animal_type, age)
            assert status == 200
            assert result['name'] == name
        else:
            raise Exception("There is no my pets")

    def test_wrong_update_self_pet_info_1(self, email=email, password=password, name='Мурзик', animal_type='Котэ', age=5):
        _, auth_key = self.pf.get_api_key(email, password)
        _, result = self.pf.get_list_of_pets(auth_key, "my_pets")
        
        if len(result['pets']) > 0:
            pet_id = result['pets'][0]['id'][::-1]
            status, result = self.pf.update_pet_info(auth_key, pet_id, name, animal_type, age)
            assert status == 400
        else:
            raise Exception("There is no my pets")

    def test_wrong_update_self_pet_info_with_wrong_auth_key(self, email=email, password=password, name='Мурзик', animal_type='Котэ', age=5):
        _, auth_key = self.pf.get_api_key(email, password)
        _, result = self.pf.get_list_of_pets(auth_key, "my_pets")
        
        if len(result['pets']) > 0:
            pet_id = result['pets'][0]['id']
            auth_key["key"] = auth_key["key"][::-1]
            status, result = self.pf.update_pet_info(auth_key, pet_id, name, animal_type, age)
            assert status == 403
        else:
            raise Exception("There is no my pets")

    def test_successful_add_new_pet_with_valid_data_without_photo(self, email=email, password=password, name='Барбоскин', animal_type='двортерьер', age=4):
        _, auth_key = self.pf.get_api_key(email, password)
        status, result = self.pf.post_new_pet_without_photo(auth_key, name, animal_type, age)
        
        assert status == 200
        assert len(result) > 0

    def test_successful_update_self_pet_photo(self, email=email, password=password, pet_photo='images/QAP_19.4.1.png'):
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
        _, auth_key = self.pf.get_api_key(email, password)
        _, result = self.pf.get_list_of_pets(auth_key, "my_pets")

        if len(result['pets']) > 0:
            pet_id = result['pets'][0]['id']
            status, result = self.pf.update_pet_photo(auth_key, pet_id, pet_photo)
            assert status == 200
            assert len(result) > 0
        else:
            raise Exception("There is no my pets")

    def test_wrong_get_api_key_for_invalid_user_1(self, email=email+"@", password=password):
        status, result = self.pf.get_api_key(email, password)
        
        assert status == 403

    def test_wrong_get_api_key_for_invalid_user_2(self, email=email, password=""):
        status, result = self.pf.get_api_key(email, password)
        
        assert status == 403

    def test_wrong_add_new_pet_with_invalid_auth_key(self, email=email, password=password, name='Барбоскин', animal_type='двортерьер', age='4', pet_photo='images/QAP_19.4.1.png'):
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
        _, auth_key = self.pf.get_api_key(email, password)
        auth_key["key"] = auth_key["key"][::-1]
        status, result = self.pf.post_new_pet(auth_key, name, animal_type, age, pet_photo)
        
        assert status == 403