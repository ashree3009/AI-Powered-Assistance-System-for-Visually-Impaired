import tensorflow as tf
import tensorflow_hub as hub
import sounddevice as sd
import numpy as np
import pandas as pd
import pyttsx3
import threading
import time

# load yamnet model
model = hub.load("https://tfhub.dev/google/yamnet/1")

# load class names
class_map = pd.read_csv(
    "https://raw.githubusercontent.com/tensorflow/models/master/research/audioset/yamnet/yamnet_class_map.csv"
)

class_names = class_map["display_name"].values

# audio settings
sample_rate = 16000
duration = 3

def speak(text):

    def run():
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        engine.stop()

    threading.Thread(target=run).start()

def record_audio():

    print("Listening...")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1
    )

    sd.wait()

    return audio.flatten()

def run_audio():

    while True:

        audio = record_audio()

        scores, embeddings, spectrogram = model(audio)

        scores = scores.numpy()

        mean_scores = np.mean(scores, axis=0)

        class_id = np.argmax(mean_scores)

        sound = class_names[class_id]

        confidence = mean_scores[class_id]

        print(f"Detected sound: {sound}  Confidence: {confidence:.2f}")

        speak(f"{sound} detected")

        time.sleep(1)