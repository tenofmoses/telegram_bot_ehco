TOKEN = '332608448:AAG42nq2uc94Fw_Ha77ZE3cDMTg27_bGbYw'
URL = 'https://api.telegram.org/bot%s/%s'

import requests


offset = 0

def api_call(method, **params):
    url = URL % (TOKEN, method)
    resp = requests.get(url, params=params).json()

    return resp['result']


while True:
    updates = api_call('getUpdates', offset=offset, timeout=10)

    if not updates:
        continue

    offset = updates[-1]['update_id']  + 1

    for update in updates:
        text = update['message']['text']
        chat_id = update['message']['chat']['id']

        api_call('sendMessage', chat_id=chat_id, text=text.upper())
