import gradio as gr

title_md = '''## **Gradio_YOLO** - Using Personal Model
<a href="https://github.com/Rahites/Gradio_YOLO">[Github]</a>
'''
def process(v):
    return v

def reset():
    return None

demo = gr.Blocks()

with demo:
    gr.Markdown(title_md)
    # 1st tab
    with gr.Tab("Webcam Live"):
        with gr.Row():
            with gr.Column():
                input_webcam = gr.Image(sources=["webcam"], streaming=True, label="Webcam")
                run_button = gr.Button()
            with gr.Column():
                output_video = gr.Video(label="Result", interactive=False)
    # 2nd tab
    with gr.Tab("Video"):
        with gr.Row():
            with gr.Column():
                input_video = gr.Video(label="Upload")
                run_button = gr.Button()
            with gr.Column():
                output_video = gr.Video(label="Result", interactive=False)

    input_video.change(fn=reset, outputs=output_video)

 
    run_button.click(fn=process,
                     inputs=[
                         input_video, 
                         ],
                     outputs=[output_video]
                     )

demo.queue().launch() #share=True