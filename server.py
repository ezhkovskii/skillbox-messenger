import time
from datetime import datetime
from flask import Flask, request, Response

from utils import filter_by_key, number_messages, number_user

app = Flask(__name__)

messages = [
    # {'name': 'Mary', 'time': time.time(), 'text': 'Привет'},
    # {'name': 'Nick', 'time': time.time(), 'text': 'Привет'},
]


@app.route("/send", methods=['POST'])
def send():
    name = request.json.get('name')
    text = request.json.get('text')
    if not (name and isinstance(name, str) and
            text and isinstance(text, str)):
        return Response(status=400)

    message = {'name': name, 'time': time.time(), 'text': text}
    messages.append(message)
    return Response(status=200)


@app.route("/messages")
def messages_view():
    try:
        after = float(request.args['after'])
    except:
        return Response(status=400)

    filtered = filter_by_key(messages, key='time', threshold=after)
    return {'messages': filtered}


@app.route("/")
def hello():
    return "Hello, World! <a href='/status'>Статус</a>"


@app.route("/status")
def status():
    return {
        'status': True,
        'name': 'Skillbox Messenger',
        'time': datetime.now().strftime('%H:%M:%S %Y/%m/%d !'),
        'num_users': number_user(messages),
        'num_messages': number_messages(messages)
    }


app.run()
