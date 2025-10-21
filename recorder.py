import pyaudio
import keyboard
import wave
import time

def record():
    audio_recordings = []

    format = pyaudio.paInt16
    channels = 1
    rate = 44100
    chunk = 1024
    output_filename = 'audio_recording.wav'
    file_path = f'audioFiles/{output_filename}'

    audio = pyaudio.PyAudio()
    stream = audio.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)
    duration = 5
    start_time = time.time()

    frames = []

    while time.time() - start_time <= duration:
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    wave_file = wave.open(file_path, 'wb')
    wave_file.setnchannels(channels)
    wave_file.setsampwidth(audio.get_sample_size(format))
    wave_file.setframerate(rate)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()

record()