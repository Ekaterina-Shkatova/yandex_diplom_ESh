# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data


# Получаем новый трек путем создания нового заказа.
def create_new_track():
    order_response = sender_stand_request.post_new_order(data.order_body) # создать новый заказ
    track_response = order_response.json().get("track") # получить track из json-тела ответа
    return track_response

# Автотест
def positive_assert():
    track_new = create_new_track() # создать новый заказ и получить трек
    data.params_get["t"] = track_new # изменить значение параметра на новый трек
    track_response = sender_stand_request.get_order(data.params_get) # получить заказ по треку
    assert track_response.status_code == 200 # сравнить код ответа с эталонным


def test_order():
    positive_assert()

# Екатерина Шкатова, 20-я когорта — Финальный проект. Инженер по тестированию плюс