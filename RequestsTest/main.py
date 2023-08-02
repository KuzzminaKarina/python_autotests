import requests

token = '56fad1c7010e42bd4511fd6706453bb6'
host = 'https://api.pokemonbattle.me:9104' # хост прода покемонов

response_add_pokemon = requests.post(f'{host}/pokemons', json = {
    "name": "Черри",
    "photo": "https://dolnikov.ru/pokemons/albums/018.png"
}, headers = {'Content-Type' : 'application/json',
              'trainer_token' : token})
print(response_add_pokemon.text) # создание покемона

response_change_trainer = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "5809",
    "name": "Мэрри",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {'Content-Type' : 'application/json',
              'trainer_token' : token})
print(response_change_trainer.text) # изменение имени покемона

response_add_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "5809"
}, headers = {'Content-Type' : 'application/json', 
              'trainer_token' : token})
print(response_add_pokeball.text) # покемон кладем в покебол

response = requests.post(f'{host}/trainers/reg', json = {
    "trainer_token": token,
    "email": "karina@kuzmina.ru",
    "password": "Iloveqa1"
}, headers = {'Content-Type' : 'application/json'})
print(response.status_code) # регистрация тренера

response_activation = requests.post(f'{host}/trainers/confirm_email', json = {
    "trainer_token": token
}, headers = {'Content-Type' : 'application/json'})
print(response_activation.text) # активация тренера

response_change_trainer = requests.put(f'{host}/trainers', json = {
    "name": "MAsh",
    "city": "Tokkyo"
}, headers = {'Content-Type' : 'application/json',
              'trainer_token' : token})
print(response_change_trainer.text) # изменение данных тренера