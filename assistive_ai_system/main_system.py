import threading

from vision.object_detection import run_vision
from audio.yamnet_live_detection import run_audio


vision_thread = threading.Thread(target=run_vision)
audio_thread = threading.Thread(target=run_audio)


vision_thread.start()
audio_thread.start()


vision_thread.join()
audio_thread.join()