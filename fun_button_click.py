from AssemblyAiHelper import transcription_from_youtube
import moviepy.editor as mp
from lyricsToPrompt import lyricsToInput
from replicateAPI import Replicate, monitorPredictionStatus
import requests

# defining the main function - its cleverly named
def fun_button_click_that_is_really_imoprtant_function_and_does_all_the_work_in_this_project_and_has_a_really_unnecessarily_long_name_to_highlight_its_importance_its_actually_a_generatoor_function_so_you_can_call_it_a_generator_of_fun_because_it_is_a_fun_project(
    url,
    assemblyAi_token,
    replicate_key,
    style
    ):
    # initial status
    status_overall = 'Downloading Youtube'
    status_transcription = 'Waiting'
    status_video = 'Waiting'
    output = [status_overall, status_transcription, status_video]
    yield output

    # Download Youtube video and transcribing
    song = transcription_from_youtube(assemblyAi_token, url)

    #Adding defined style to song
    song['style'] = style

    status_overall = 'Transcribed, waiting for the Video'
    status_transcription = 'Done'
    status_video = 'In progress'
    output = [status_overall, status_transcription, status_video]
    yield output

    # Generate Video
    prompt, movement, max_frame = lyricsToInput().makeOutput(song['sentences'], song['style'].lower(), song['title'])
    prediction = Replicate(replicate_key).callDeforumOnReplicate(prompt=prompt, angle=movement['angle'], zoom=movement['zoom'],
    translation_x=movement['translation_x'], translation_y=movement['translation_y'], max_frames=max_frame)
    video = monitorPredictionStatus(prediction)
    video_file = requests.get(video)
    open("out_1.mp4", 'wb').write(video_file.content)

    
    status_overall = 'Transcribed, waiting for the Video'
    status_transcription = 'Done'
    status_video = 'Done, You can click the button below'
    output = [status_overall, status_transcription, status_video]
    yield output

fun_generator = fun_button_click_that_is_really_imoprtant_function_and_does_all_the_work_in_this_project_and_has_a_really_unnecessarily_long_name_to_highlight_its_importance_its_actually_a_generatoor_function_so_you_can_call_it_a_generator_of_fun_because_it_is_a_fun_project

def load_video():
    #Input audio file
    audio = mp.AudioFileClip('audio.mp3')
    #Input video file
    video = mp.VideoFileClip('out_1.mp4')
    #adding external audio to video
    final_video = video.set_audio(audio)
    #Extracting final output video
    final_video.write_videofile("output_video.mp4")
    return 'output_video.mp4'