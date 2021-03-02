import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

class PetFriends:
    def __init__(self):
        self.url = "https://petfriends1.herokuapp.com/"

    def get_api_key(self, email: str, password: str) -> tuple((int, dict)):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
        с уникальным ключем пользователя, найденного по указнным email и password"""
        
        header = {
            "email": email,
            "password" : password
        }
        res = requests.get(self.url + 'api/key', headers=header)
        status = res.status_code
        api_key = ""
        try:    api_key = res.json()
        except: api_key = res.text
        return status, api_key

    def get_list_of_pets(self, auth_key, filters: str = "") -> (int, dict):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
        со всеми питомцами, найденными по указнным auth_key и filters"""
        
        header = {"auth_key" : auth_key["key"]}
        filters = {"filters" : filters}
        res = requests.get(self.url + 'api/pets', headers=header, params=filters)
        status = res.status_code
        result = ""
        try:    result = res.json()
        except: result = res.text
        return status, result

    def post_new_pet(self, auth_key, name: str, animal_type: str, age: int, pet_photo) -> (int, dict):
        """Метод использует API сервера для возврата статуса запроса и добавлении
        нового питомца с данными auth_key, name, animal_type, age, pet_photo"""
        
        data = MultipartEncoder(
         fields={
            'name': name,
            'animal_type': animal_type,
            'age': str(age),
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
         })
        header = {
            "auth_key" : auth_key["key"],
            "Content-Type": data.content_type
        }
        res = requests.post(self.url + 'api/pets', headers=header, data=data)
        status = res.status_code
        result = ""
        try:    result = res.json()
        except: result = res.text
        return status, result

    def delete_pet(self, auth_key, pet_id: str) -> int:
        """Метод использует API сервера для возврата статуса запроса
        и удалении питомца по указнным auth_key и pet_id"""

        header = {
            "auth_key" : auth_key["key"]
        }
        res = requests.delete(self.url + f'api/pets/{pet_id}', headers=header)
        status = res.status_code
        return status

    def update_pet_info(self, auth_key, pet_id: str, name: str, animal_type: str, age: int) -> (int, dict):
        """Метод использует API сервера для возврата статуса запроса и обновлении данных
        у питомца по указнным auth_key и pet_id на данные в полях name, animal_type, age"""

        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
         }
        header = {
            "auth_key" : auth_key["key"]
        }
        res = requests.put(self.url + f'api/pets/{pet_id}', headers=header, data=data)
        status = res.status_code
        result = ""
        try:    result = res.json()
        except: result = res.text
        return status, result

    def post_new_pet_without_photo(self, auth_key, name: str, animal_type: str, age: int) -> (int, dict):
        """Метод использует API сервера для возврата статуса запроса и добавлении
        нового питомца с данными auth_key, name, animal_type, age"""
        
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
         }
        header = {
            "auth_key" : auth_key["key"],
        }
        res = requests.post(self.url + 'api/create_pet_simple', headers=header, data=data)
        status = res.status_code
        result = ""
        try:    result = res.json()
        except: result = res.text
        return status, result

    def update_pet_photo(self, auth_key, pet_id: str, pet_photo) -> (int, dict):
        """Метод использует API сервера для возврата статуса запроса и обновлении pet_photo
        у питомца по указнным auth_key и pet_id"""

        data = MultipartEncoder(
         fields={
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
         })
        header = {
            "auth_key" : auth_key["key"],
            "Content-Type": data.content_type
        }
        res = requests.post(self.url + f'api/pets/set_photo/{pet_id}', headers=header, data=data)
        status = res.status_code
        result = ""
        try:    result = res.json()
        except: result = res.text
        return status, result