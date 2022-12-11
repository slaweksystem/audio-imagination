from AssemblyAi import *
import pandas as pd
import youtube
from time import sleep

def transcription_from_youtube(token, url):

    # download a song from youtube
    song = youtube.youtube_download(url)

    # Send mp3 to the AssemblyAI API:
    initial_send = send_local_file('audio.mp3', token)

    # get id from the responce
    id = json.loads(initial_send)['id']

    # Bad method to check the status - to be improved in the future
    while True:
        sleep(60)
        result = get_result(id, token)
        if result['status'] == 'completed':
            break
    
    # Dividing text into sections with timestamps, n wrds at the time
    sentences = sentence_div(result['words'], 6)

    song['sentences'] = sentences
    return song




def sentence_div(words, words_per_sentence = 5):
    sentences = []
    words_per_sentence = 5
    i = 0
    
    
    # bizzare loop to create sentances from words with timestamps
    # the goal was to have at least n words in one statement
    while i < len(words):
        j = 0
        sentence = ''
        start = words[i]['start']
        while j < words_per_sentence or \
            i < len(words):
            #print(result['words'][i]['text'])
            sentence += words[i]['text'] + ' '
            i += 1
            j += 1
            if (j > words_per_sentence or i >= len(words)) and \
                ('.' in words[i-1]['text'] or \
                '?' in words[i-1]['text'] or \
                ',' in words[i-1]['text']):
                #print(sentence)
                end = words[i-1]['end']
                sentences.append({'sentence' : sentence,
                                    'start' : start,
                                    'end'   : end} )
                break
    return sentences