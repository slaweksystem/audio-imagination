import gradio as gr
import descriptionsGui as des_gui
from fun_button_click import fun

# Delete dis
token = '29d4559a6dca46e0850c9f1d3b8944f4'
replicate_key = 'abc'


with gr.Blocks() as demo:
    variables = {}
    gr.Markdown("# Audio Imagination Demo")
    gr.Text(des_gui.text_config, label = 'Configuration')
    variables['url'] = gr.Textbox(label="Youtube url")
    variables['assemblyAi_token'] = gr.Textbox(label="Assembly Ai token", value=token)
    variables['replicate_key'] = gr.Textbox(label="Replicate Key", value = replicate_key)
    button = gr.Button("Give me a Video")

    txt_box_youtube_download = gr.Textbox(label = 'Youtube', value = 'Not Started')
    txt_box_transcription = gr.Textbox(label = 'Transcription', value = 'Not Started')
    txt_box_video_generatr = gr.Textbox(label = 'Video', value = 'Not Started')
    
    button.click(fun, inputs = variables, 
                    outputs = [txt_box_youtube_download,
                    txt_box_transcription,
                    txt_box_video_generatr])

demo.queue()

demo.launch() 

