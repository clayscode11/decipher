import pyaudio
import keyboard
import wave
import time

audio_recordings = []

format = pyaudio.paInt16 # 16 bit
channels = 1 # mono audio channel
rate = 44100 # Sample rate
chunk = 1024 # frames in buffer
output_filename = "recordedFile.wav" # file name provsioning

audio = pyaudio.PyAudio() # init pyaudio
stream = audio.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk) # opening the new audio stream

frames = []
print("Press SPACE to start recording")
keyboard.wait("space")
print("Recording... Press SPACE to end recording.")
time.sleep(0.2) # gives buffer to account for physical input delays




