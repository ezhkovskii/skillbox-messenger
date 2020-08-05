import requests

name = input('name: ')

while True:
    text = input()
    data = {'name': name, 'text': text}

    requests.post('http://127.0.0.1:5000/send', json=data)
