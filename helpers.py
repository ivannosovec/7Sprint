import random
import allure

@allure.step('Генерация валидных данных курьера')
def generate_courier_data():
    login = f'courier{random.randint(100000, 999999)}'
    password = "123321123qq"
    first_name = "Alexandr"
    return {"login": login, "password": password, "firstName": first_name}