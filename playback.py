import winsound

def playback():
    winsound.PlaySound('audioFiles/audio_recording.wav', winsound.SND_FILENAME)

playback()