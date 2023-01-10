import requests
import json

my_api = 'cbr-xml-daily.ru'

def getRequest(api_server, type, method):
    try:
        if type=='GET':
            send_url = requests.get(f'https://{api_server}/{method}')
            return send_url.text
        elif type=='POST':
            send_url = requests.post(f'https://{api_server}/{method}')
            return send_url.text
        else:
            return print('ErrorType')
    except Exception as e:
        return print('ErrorURL: {e}')

def getJson(self):
    try:
        return json.loads(self)
    except Exception as e:
        return print(f'ErrorJSON: {e}')

get_json = getRequest(
    api_server=my_api,
    type='GET',
    method='daily_json.js'
)
json_data = getJson(get_json)