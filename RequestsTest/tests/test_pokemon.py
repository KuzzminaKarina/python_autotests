import requests
import pytest

token = '56fad1c7010e42bd4511fd6706453bb6'
host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers', params = {'trainer_id' : 1903})
    assert response.status_code == 200

def test_part_of_answer(): 
    response = requests.get(f'{host}/trainers', params = {'trainer_id' : 1903})
    assert response.json()['trainer_name'] == 'MAsh' 
    assert response.json()['city'] == 'Tokkyo' 

@pytest.mark.parametrize('key, value', [('name', 'Мэрри'), 
                                        ('trainer_id', '1903'), 
                                        ('attack', '1.0')])

def test_parts_of_answer(key, value):
    response = requests.get(f'{host}/pokemons', params = {'trainer_id' : 1903})
    assert response.json()[0][key] == value