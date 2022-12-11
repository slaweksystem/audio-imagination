import requests
import json

def transcribe_url(url, token):

    endpoint = "https://api.assemblyai.com/v2/transcript"

    json = {
      "audio_url": url,
      "auto_highlights": True,
      "iab_categories": True,
      "sentiment_analysis": True,
      "summarization": True,
      "summary_model": "informative",
      "summary_type": "bullets"

    }

    headers = {
      "Authorization": token,
      "Content-Type": "application/json"
    }

    response = requests.post(endpoint, json=json, headers=headers)
    return response.content.decode('utf-8')

def send_local_file(filename, token):
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    headers = {'authorization': token}
    response = requests.post('https://api.assemblyai.com/v2/upload',
                            headers=headers,
                            data=read_file(filename))

    return transcribe_url(response.json()['upload_url'], token)

def get_result(id, token):
    endpoint = f'https://api.assemblyai.com/v2/transcript/{id}'
    headers = {
        "authorization": token,
    }
    response = requests.get(endpoint, headers=headers)
    return json.loads(response.content.decode('utf-8'))

def get_list(token):
    endpoint = 'https://api.assemblyai.com/v2/transcript'
    headers = {
        "authorization": token,
    }
    response = requests.get(endpoint, headers=headers)
    return json.loads(response.content.decode('utf-8'))

def delete(id, token):
    endpoint = f'https://api.assemblyai.com/v2/transcript/{id}'
    headers = {
        "authorization": token,
    }
    response = requests.delete(endpoint, headers=headers)
    return response