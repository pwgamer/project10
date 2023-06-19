import requests
from configuration import BASE_URL, USER_PATH, KIT_PATH
from data import headers

# Функция для создания нового пользователя
def create_new_user(user_body):
    url = BASE_URL + USER_PATH
    response = requests.post(url, json=user_body, headers=headers)
    return response.json()["authToken"]

# Функция для создания нового набора
def post_new_client_kit(kit_body, auth_token):
    url = BASE_URL + KIT_PATH
    headers["Authorization"] = f"Bearer {auth_token}"
    response = requests.post(url, json=kit_body, headers=headers)
    return response



