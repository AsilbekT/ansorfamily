from celery import Task
import requests
from bot.credentials import TOKEN
from celery import shared_task

def send_photo(img_path, chat_id, caption):
    api_url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    files = {'photo': open(img_path, 'rb')}
    payload = {
        'chat_id': chat_id,
        'caption': caption,
        'parse_mode': 'HTML'
    }
    response = requests.post(api_url, data=payload, files=files)

    json_response = response.json()

    if 'result' in json_response and 'photo' in json_response['result']:
        file_id = json_response['result']['photo'][-1]['file_id']
        return file_id

    return ""

@shared_task
def send_photo_by_id(file_id, chat_id, caption):
    api_url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    payload = {
        'chat_id': chat_id,
        'photo': file_id,
        'caption': caption,
        'parse_mode': 'html'
    }
    response = requests.post(api_url, data=payload)

    return response


