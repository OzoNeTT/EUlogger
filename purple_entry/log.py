import requests

from config.config import PURPLE_ENTRY_URL, PURPLE_ENTRY_TOKEN


def add_log(string, type_name='DEBUG'):
    json = {
        'project-token': PURPLE_ENTRY_TOKEN,
        'title': string,
        'type': type_name,
    }
    requests.post(f'{PURPLE_ENTRY_URL}/log/create', json=json)
