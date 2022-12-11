import gradio as gr
import descriptionsGui as des_gui
from fun_button_click import fun_generator
from fun_button_click import load_video

# Delete dis
v_token = '29d4559a6dca46e0850c9f1d3b8944f4'
v_replicate_key = 'abc'
v_url = 'https://www.youtube.com/watch?v=kNLdd0LUiTI'

def click(url):

    return [url['a'],url['a'],url['a']]

with gr.Blocks() as demo:
    variables = {}
    gr.Markdown("# Audio Imagination Demo")
    gr.Text(des_gui.text_config, label = 'Configuration')
    url = gr.Textbox(label="Youtube url", value = v_url)
    assemblyAi_token = gr.Textbox(label="Assembly Ai token", value=v_token)
    replicate_key = gr.Textbox(label="Replicate Key", value = v_replicate_key)
    style = gr.Dropdown(choices = des_gui.styles)
    button_fun = gr.Button("Generate me a Video")
    

    txt_box_youtube_download = gr.Textbox(label = 'Youtube', value = 'Not Started')
    txt_box_transcription = gr.Textbox(label = 'Transcription', value = 'Not Started')
    txt_box_video_generatr = gr.Textbox(label = 'Video', value = 'Not Started')

    button_give_me_vid = gr.Button("Give me my Video")
    
    video = gr.Video(interactive = False)

    button_fun.click(fun_generator, inputs = [
                            url,
                            assemblyAi_token,
                            replicate_key,
                            style
                            ], 
                    outputs = [txt_box_youtube_download,
                    txt_box_transcription,
                    txt_box_video_generatr])

demo.queue()

demo.launch() 

