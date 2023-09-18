from flask import Flask, render_template, request, send_file, send_from_directory
from ttsmms import TTS
import subprocess
import os
import wavio
import datetime

app = Flask(__name__)

# Define the directory to store language models
LANGUAGE_MODELS_DIRECTORY = 'language_models'

def download_language_model(language_key):
    language_model_path = os.path.join(LANGUAGE_MODELS_DIRECTORY, f'{language_key}.tar.gz')

    # Check if the language model is already downloaded
    if not os.path.exists(language_model_path):
        # Language model not found, download it
        subprocess.call(['curl', f'https://dl.fbaipublicfiles.com/mms/tts/{language_key}.tar.gz', '--output', language_model_path])

    return language_model_path

def convertTextToAudio(language_key, text):
    # Download or use the existing language model
    language_model_path = download_language_model(language_key)

    # Extract the language model if necessary
    if not os.path.exists(f'data/{language_key}'):
        subprocess.call(['mkdir', '-p', 'data'])
        subprocess.call(['tar', '-xzf', language_model_path, '-C', 'data/'])

    # Initialize the TTS with the language model
    tts = TTS(f'data/{language_key}')
    wav_text = tts.synthesis(text)

    # Specify the directory to save the audio
    save_directory = './speech'

    # Ensure the directory exists, create it if it doesn't
    os.makedirs(save_directory, exist_ok=True)

    # Generate a unique audio file name based on date, time, and language
    now = datetime.datetime.now()
    audio_file_name = "{}_{}_{}.wav".format(now.strftime("%Y%m%d_%H%M%S"), language_key, text[:10])  # You can adjust the format as needed

    # Define the file path for the saved audio
    audio_file_path = os.path.join(save_directory, audio_file_name)

    # Save the audio to the specified file path with the correct sampling rate
    wavio.write(audio_file_path, wav_text["x"], wav_text["sampling_rate"], sampwidth=2)

    return audio_file_path, audio_file_name

@app.route("/", methods=["GET", "POST"])
def index():
    audio = None
    audio_file_name = None

    if request.method == "POST":
        language_key = request.form["language"]
        text = request.form["text"]
        audio_file_path, audio_file_name = convertTextToAudio(language_key, text)

        # Serve the saved audio file
        audio = "/speech/" + audio_file_name

    return render_template("index.html", audio=audio, audio_file_name=audio_file_name)

@app.route('/audio/<filename>')
def audio(filename):
    return send_from_directory('speech', filename)

if __name__ == "__main__":
    app.run(debug=True)
