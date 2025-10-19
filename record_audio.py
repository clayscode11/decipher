import pyaudio
import keyboard
import wave
import time
import winsound

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

while True:
    try:
        data = stream.read(chunk)
        frames.append(data)
    except KeyboardInterrupt:
        break
    if keyboard.is_pressed('space'):
        print("Stopping recording after a brief delay")
        print("Press enter to play the recording")
        time.sleep(0.2)
        

    stream.stop_stream()
    stream.close()  
    audio.terminate()

    wave_file = wave.open(output_filename, "wb")
    wave_file.setnchannels(channels)
    wave_file.setsampwidth(audio.get_sample_size(format))
    wave_file.setframerate(rate)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()

    if keyboard.is_pressed('enter'):
        try:
            winsound.PlaySound('recordedFile.wav', winsound.SND_FILENAME)
        except Exception:
            print("Error playing recorded file")