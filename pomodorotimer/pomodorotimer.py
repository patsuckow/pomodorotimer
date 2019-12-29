"""
Created by Alexey Patsukov (patsuckow@yandex.ru) 🇷🇺
"""
import os
import sys
import time
import subprocess
from collections import deque
from pydub import AudioSegment, generators
from pydub.playback import play

try:
    assert sys.version_info >= (3, 6)
except Exception:
    raise SystemExit('PomodoroTimer works with Python 3.6 or higher.')


class PomodoroTimer:
    """
    Console Pomodoro timer with playing the melody of the signal or with
    the generation of an end time signal. Displays a push notification on
    Linux and Mac OS X.

    Pomodoro Technique - see: https://en.wikipedia.org/wiki/Pomodoro_Technique
    """
    ALARM_FILENAME = os.path.realpath('.local/tic-tic.wav')

    def __init__(self) -> None:
        mess = "Enter a time in minutes for your Pomodoro: "
        self.stack_watch = deque(list('🕛🕧🕐🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥🕚🕦'))
        try:
            while True:
                try:
                    self.timer(int(input(mess)))
                except ValueError:
                    print("Wrong input. Try again.")
        except KeyboardInterrupt:
            print("\nPomodoro's timer work has been interrupted.")

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
        play(AudioSegment.from_wav(PomodoroTimer.ALARM_FILENAME))

    def reverse_timer(self, sec: int) -> None:
        """
        - Clear up string and hide console cursor
        - Countdown
        - Clear string and show console cursor
        """
        self.write_flush(f"\x1b[A{45*' '}\r\x1b[?25l")
        for i in range(sec, 0, -1):
            self.write_flush(f'\r {self.animated_clock()}{self.lead_time(i)} ')
            time.sleep(1)
        self.write_flush(f"\r{30*' '}\r\x1b[?25h")

    @staticmethod
    def write_flush(string: str) -> None:
        """Don't repeat yourself"""
        sys.stdout.write(string)
        sys.stdout.flush()

    @staticmethod
    def lead_time(sec: int) -> str:
        """Elapsed Time Calculation"""
        return f" Pomodoro timer: min: " \
               f"\x1b[32m\x1b[1m{int(sec // 60)}\x1b[0m, sec: " \
               f"\x1b[32m\x1b[1m{round(sec % 60, 3)}\x1b[0m"

    def animated_clock(self) -> str:
        """
        To extract the first element from the list and place it at the end of
        the list, for greater performance, we will use the stack instead of
        the standard list methods .append() and .pop().
        https://docs.python.org/3/library/collections.html?#collections.deque
        """
        clock = self.stack_watch[0]
        self.stack_watch.appendleft(self.stack_watch.pop())

        return clock

    def timer(self, minutes: int) -> None:
        """Run reverse timer.

        Setting the time for the Pomodoro timer.
        Push-notifications on Linux desktop or console.
        Play either mp3 file or generated sound.
        Clear console before new setup Pomodoro timer.

        Console cleaning could be written shorter: os.system('cls||clear')
        """
        self.reverse_timer(minutes * 60)
        title = '⏰ Pomodoro: '
        info = f"{minutes} min TIME'S UP!"
        mes = title + info + "\n"
        if os.path.exists(PomodoroTimer.ALARM_FILENAME):
            self.wav_sound()
        else:
            self.default_sound()

        if sys.platform in ('linux', 'osx'):
            subprocess.call('clear', shell=True)
            subprocess.call(['notify-send', title, info])
        elif sys.platform in ('nt', 'dos', 'ce'):
            subprocess.call('cls', shell=True)
            print(mes)
        else:
            print('\n', mes)
