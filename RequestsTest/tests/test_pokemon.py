import requests
import pytest

token = '56fad1c7010e42bd4511fd6706453bb6'
host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}//trainers', params = {'trainer_id' : 1903})
    assert response.status_code == 200

def test_name_in_answer(): 
    response = requests.get(f'{host}//trainers', params = {'trainer_id' : 1903})
    assert response.json()['trainer_name'] == 'MAsh' 
    assert response.json()['city'] == 'Tokkyo' 


    