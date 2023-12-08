![Ilaria AI Suite](./ilariaaisuite.png)
***
[![Static Badge](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Space-s?labelColor=YELLOW&color=FFEA00)](https://huggingface.co/spaces/TheStinger/Ilaria_TTS) [![Static Badge](https://img.shields.io/badge/%F0%9F%A4%97%20HF%20Space-Duplication-s?labelColor=YELLOW&color=FFEA00)](https://huggingface.co/spaces/TheStinger/Ilaria_TTS?duplicate=true) [![Static Badge](https://img.shields.io/badge/GitHub-Source%20Code-s?logo=GitHub)](https://github.com/TheStingerX/Ilaria-TTS) [![Static Badge](https://img.shields.io/badge/AI%20Hub-Discord%20Server-s?logo=Discord&color=%09%237289da)](https://discord.gg/aihub) [![Static Badge](https://img.shields.io/badge/Ko--Fi-s?logo=Ko-Fi&label=Support%20me%20on&labelColor=434b57&color=FF5E5B)](https://ko-fi.com/ilariaowo)
***
<p align="center">
  <h1>Ilaria TTS 💖</h1>
</p>

🎉 Welcome to Ilaria TTS! 🎉  
  
This project leverages various libraries and modules to create a Graphical User Interface (GUI) for Text-to-Speech.  
It's primarily designed for use with HuggingFace Spaces. 🤗   

Ilaria TTS is part of the Ilaria AI Suite wich includes various easy and powerful tools. 💖

## 📦 Installation 📦

To use this project, clone the original Space on Hugging Face.  
Make sure you restart it time to time to keep up with the new updates.

## 🖥️ Usage 🖥️

Once the dependencies are installed automatically, Hugging Face will use app.py to start the user interface.  
From there, you can utilize the various features of the project.

## 🌟 Features 🌟

Ilaria TTS offers a range of features, including:

- 🗣️ **Text-to-Speech Conversion**:  
The code uses the Communicate class from the edge_tts module to convert text to speech.
The text_to_speech_edge function takes a text and a language code as input, and returns the input text and the path of the generated speech audio file.

- 🌍 **User-Friendly Web Interface**:  
The code uses the gradio module to create an intuitive web interface.
Users can easily input text and choose the language, and the application will return the input text and the generated speech audio.

- 🖥️ **User-Friendly Web Interface**:  
Ilaria TTS uses the gradio module to create an intuitive web interface.
Users can easily upload an image, and the application will return the upscaled and restored image.

- 📂 **Efficient File Handling**:  
The code uses the tempfile module to create a temporary file for the generated speech audio.
The NamedTemporaryFile function is used with the delete=False option, which means the file won’t be deleted when it is closed.  
This allows the audio file to be saved and returned to the user.

- 🚀 **Asynchronous Execution**:  
The code uses the anyio module to run the web interface in an asynchronous manner.
This allows the application to handle multiple requests concurrently, improving the overall performance and responsiveness of the application.

## 🙏 Credits 🙏

- **Squishy** - For helping me with the ideas

## 🤝 Contributing 🤝

Interested in contributing to this project? Ilaria is always looking for collaborators.  
Feel free to open a pull request on Hugging Face.

## 📄 License 📄

This project is released under the `INCU` license.  
For more details, please check the license file.  
For further questions feel free to contact Ilaria.
