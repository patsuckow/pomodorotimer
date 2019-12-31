import os
from pydub import AudioSegment, generators
from pydub.playback import play


class Sound:

    # Why path to wav is '.local/tic-tic.wav' ? - since in setup.py with the
    # option data_files=['tic-tic.wav'] we set that the file must be sent
    # to .local/
    ALARM_FILENAME = os.path.realpath('.local/tic-tic.wav')

    def __init__(self):
        if os.path.exists(Sound.ALARM_FILENAME):
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

    @staticmethod
    def wav_sound() -> None:
        """Play wav file"""
        play(AudioSegment.from_wav(Sound.ALARM_FILENAME))


if __name__ == "__main__":
    Sound()
