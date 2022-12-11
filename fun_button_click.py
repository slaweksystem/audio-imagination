from AssemblyAiHelper import transcription_from_youtube
import moviepy.editor as mp

# defining the main function - its cleverly named
def fun_button_click_that_is_really_imoprtant_function_and_does_all_the_work_in_this_project_and_has_a_really_unnecessarily_long_name_to_highlight_its_importance_its_actually_a_generatoor_function_so_you_can_call_it_a_generator_of_fun_because_it_is_a_fun_project(
    url,
    assemblyAi_token,
    replicate_key
    ):
    # initial status
    status_overall = 'Downloading Youtube'
    status_transcription = 'Waiting'
    status_video = 'Waiting'
    output = [status_overall, status_transcription, status_video]
    yield output

    # Download Youtube video and transcribing
    song = transcription_from_youtube(assemblyAi_token, url)

    status_overall = 'Transcribed, waiting for the Video'
    status_transcription = 'Done'
    status_video = 'In progress'
    output = [status_overall, status_transcription, status_video]
    yield output

    # Generate Video

    # Place for Jakubs Work

    status_overall = 'Transcribed, waiting for the Video'
    status_transcription = 'Done'
    status_video = 'Done, You can click the buttn below'
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