import re
import requests

def filter_by_key(elements, key, threshold):
    filtered_elements = []

    for element in elements:
        if element[key] > threshold:
            filtered_elements.append(element)

    return filtered_elements


def max_by_key(elements, key):
    if not elements:
        return None

    m = elements[0]
    for element in elements:
        if m[key] < element[key]:
            m = element
    return m


def number_user(messages):
    num_names = []
    for d in messages:
        num_names.append(d['name'])
    return len(set(num_names))

def number_messages(messages):
    return len(messages)

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url
