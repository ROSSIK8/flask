import requests

HOST_PORT = 'http://127.0.0.1:8000'


def post():
    post_data = {
        'title': 'Название',
        'description': 'Описание',
        'owner': 'Владелец'
    }
    response = requests.post(f'{HOST_PORT}/advertisements', json=post_data)
    print(response.json())


def get(id: int):
    response = requests.get(f'{HOST_PORT}/advertisements/{id}/')
    print(response.json())


def delete(id: int):
    response = requests.delete(f'{HOST_PORT}/advertisements/{id}/')
    print(response.json())


post()

get(1)

delete(1)
