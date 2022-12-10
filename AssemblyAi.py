import requests
import json

def transcribe_url(url, token):

    endpoint = "https://api.assemblyai.com/v2/transcript"

    json = {
      "audio_url": url
    }

    headers = {
      "Authorization": token,
      "Content-Type": "application/json"
    }

    response = requests.post(endpoint, json=json, headers=headers)
    return response.content.decode('utf-8')

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