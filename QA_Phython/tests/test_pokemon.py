import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2df0b40ab576940822ca8a126c63b596'
HEADERS = {"Trainer_Token": TOKEN, 'Content-Type': 'application/json'}
TRAINER_ID = '7030'
TRAINER_NAME = 'VanGun'

def test_status_code():
    response = requests.get(
        url=f'{URL}/trainers',
        headers=HEADERS,
        params={'trainer_id': TRAINER_ID}) 
    assert response.status_code == 200

def test_trainer_name():
    response_name = requests.get(
        url=f'{URL}/me',
        headers=HEADERS,
        params={'trainer_id': TRAINER_ID}) 
    assert response_name.json()['data'][0]['trainer_name'] == TRAINER_NAME