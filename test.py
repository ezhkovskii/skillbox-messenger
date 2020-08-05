import random
from utils import filter_by_key, max_by_key

print(random.randint(1, 5))

messages = [
    {'name': 'Jack', 'time': 1596472258, 'text': 'Привет'},
    {'name': 'Mary', 'time': 1596472261, 'text': 'Привет!'},
    {'name': 'Nick', 'time': 1596472260, 'text': 'Привет всем!'},
]


print(filter_by_key(messages, 'time', 1596472258))
print(filter_by_key(messages, 'time', 1596472259))
print(filter_by_key(messages, 'time', 1596472260))
print(filter_by_key(messages, 'time', 1596472261))

print(max_by_key(messages, 'time'))
print(max_by_key([], 'time'))
