import requests
from faker import Faker
fake = Faker()
random_name = fake.name()
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2df0b40ab576940822ca8a126c63b596'
HEADERS = {"Trainer_Token": TOKEN, 'Content-Type': 'application/json'}

BODY_create = {
    "name": random_name,
    "photo_id": -1}

response_create = requests.post(url=f'{URL}/pokemons', 
                                headers=HEADERS, json=BODY_create)
print(response_create.text)
pokemon_id = response_create.json()["id"]

BODY_rename = {
    "pokemon_id": pokemon_id,
    "name": random_name,
    "photo_id": -1 }
response_rename = requests.put(url=f'{URL}/pokemons', 
                                headers=HEADERS, json=BODY_rename)
print(response_rename.text)

BODY_pokeball = {"pokemon_id": pokemon_id}
response_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', 
                                headers=HEADERS, json = BODY_pokeball)
print(response_pokeball.text)