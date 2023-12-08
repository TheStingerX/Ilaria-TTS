
from tts_voice import tts_order_voice
import edge_tts
import gradio as gr
import tempfile
import anyio

language_dict = tts_order_voice

async def text_to_speech_edge(text, language_code):
    voice = language_dict[language_code]
    communicate = edge_tts.Communicate(text, voice)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tmp_path = tmp_file.name

    await communicate.save(tmp_path)

    return "Text input：{}".format(text), tmp_path



input_text = gr.inputs.Textbox(lines=5, label="Text")
output_text = gr.outputs.Textbox(label="Text input")
output_audio = gr.outputs.Audio(type="filepath", label="Audio output")
default_language = list(language_dict.keys())[0]
language = gr.inputs.Dropdown(choices=list(language_dict.keys()), default=default_language, label="Choose the language and the model")


interface = gr.Interface(fn=text_to_speech_edge, inputs=[input_text, language], outputs=[output_text, output_audio], title="Ilaria TTS 💖")


if __name__ == "__main__":
    anyio.run(interface.launch, backend="asyncio")