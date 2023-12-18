import os
import sounddevice as sd
import numpy as np
from scipy.io import wavfile

class Sound:
    def __init__(self):
        self.path = os.path.abspath(os.path.join(os.path.dirname(__file__), "tic-tic.wav"))
        if os.path.exists(self.path):
            self.play_wav_sound()
        else:
            self.play_default_sound()

    @staticmethod
    def play_default_sound() -> None:
        """
        Sound generation with a frequency of 432 Hz and a duration of 864 milliseconds
        """
        frequency = 432
        duration = 0.864
        # Timeline (44100 Hz - sampling rate)
        t = np.linspace(0, duration, int(44100 * duration), endpoint=False)
        # Generation of sinusoidal sound
        data = 0.5 * np.sin(2 * np.pi * frequency * t)
        # Playback
        sd.play(data, 44100)
        # Waiting for the playback to end
        sd.wait()
    
    def play_wav_sound(self) -> None:
        """Play wav file"""
        # Reading audio file
        fs, data = wavfile.read(self.path)
        # Playback
        sd.play(data, fs)
        # Waiting for the playback to end
        sd.wait()

if __name__ == "__main__":
    Sound()