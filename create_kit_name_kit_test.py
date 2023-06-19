import data
from sender_stand_request import create_new_user, post_new_client_kit


# Функция для изменения имени в запросе
def get_kit_body(name_value):
    return {"name": name_value}


# Функция для получения токена нового пользователя
def get_new_user_token():
    return create_new_user(data.user_body)


# Функция для позитивной проверки значений
def positive_assert(kit_body):
    auth_token = get_new_user_token()
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    response_json = response.json()
    assert response_json["name"] == kit_body["name"]


# Функция для негативной проверки кода ответа 400
def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400


# ТК-1 Допустимое количество символов (1):
def test_name_length_1():
    positive_assert(data.kit_body_length_1)


# ТК-2 Допустимое количество символов (511):
def test_name_length_511():
    positive_assert(data.kit_body_length_511)


# ТК-3 Количество символов меньше допустимого (0):
def test_name_empty():
    negative_assert_code_400(data.kit_body_empty)


# ТК-4 Количество символов больше допустимого (512):
def test_name_length_512():
    negative_assert_code_400(data.kit_body_length_512)


# ТК-5 Разрешены английские буквы:
def test_name_english_letters():
    positive_assert(data.kit_body_english_letters)


# ТК-6 Разрешены русские буквы:
def test_name_russian_letters():
    positive_assert(data.kit_body_russian_letters)


# ТК-7 	Разрешены спецсимволы:
def test_name_special_characters():
    positive_assert(data.kit_body_special_letters)


# ТК-8 Разрешены пробелы:
def test_name_with_spaces():
    positive_assert(data.kit_body_with_spaces)


# ТК-9 Разрешены цифры:
def test_name_numeric_characters():
    positive_assert(data.kit_body_numeric)


# ТК-10 Параметр не передан в запросе:
def test_empty_body():
    negative_assert_code_400(data.kit_body_empty_body)


# ТК-11 Передан другой тип параметра (число):
def test_name_integer_type():
    negative_assert_code_400(data.kit_body_integer)
