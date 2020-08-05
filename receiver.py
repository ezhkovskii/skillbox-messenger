import time
from datetime import datetime

import requests
from utils import get_image_url
import webbrowser



def pretty_message(message):
    dt = datetime.fromtimestamp(message['time'])
    dt_str = dt.strftime('%H:%M:%S')
    print(message['name'], dt_str)
    print(message['text'])
    print()

    if message['text'] == 'бот пришли пёсика':
        url = get_image_url()
        webbrowser.open(url)

after = 0.0
while True:
    data = requests.get('http://127.0.0.1:5000/messages',
                        params={'after': after}).json()

    for message in data['messages']:
        pretty_message(message)
        after = message['time']

    time.sleep(1)
