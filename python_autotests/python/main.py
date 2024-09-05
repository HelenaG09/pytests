import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6d3dcee639af34d2f7829b3eef91a5d4'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "helena0978@yandex.ru",
    "password": "Pasena1305",
}
body_confirmation = {
    "trainer_token": TOKEN
                     }
body_create = {
    "name": "generate",
    "photo_id": -1
}

body_change = {
    "pokemon_id": "67869",
    "name": "МИГ",
    "photo_id": 2
}

body_add = {
    "pokemon_id": "67865"
}



response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)

response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

message = response_change.json()['message']
print(message)

response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(response_add.text)

message = response_add.json()['message']
print(message)
