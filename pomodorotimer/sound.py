import os
from pydub import AudioSegment, generators
from pydub.playback import play


class Sound:
    def __init__(self):
        self.path = os.path.dirname(__file__) + '/tic-tic.wav'
        if os.path.exists(self.path):
            self.wav_sound()
        else:
            self.default_sound()

    @staticmethod
    def default_sound() -> None:
        """
        It will be used when the wav file is not been found.
        Default: Frequency 432 Hz, duration=864 milliseconds.
        """
        play(generators.Sine(432).to_audio_segment(duration=864))

    def wav_sound(self) -> None:
        """Play wav file"""
        play(AudioSegment.from_wav(self.path))


if __name__ == "__main__":
    Sound()
