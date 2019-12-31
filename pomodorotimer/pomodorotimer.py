"""
Created by Alexey Patsukov (patsuckow@yandex.ru) 🇷🇺
"""
import os
import sys
import time
import subprocess
from collections import deque

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

    def __init__(self) -> None:
        # Clear console before setup Pomodoro timer
        if sys.platform in ('linux', 'osx'):
            subprocess.call('clear', shell=True)
        elif sys.platform in ('nt', 'dos', 'ce'):
            subprocess.call('cls', shell=True)

        mess = " Enter a time in minutes for your Pomodoro: "
        self.stack_watch = deque(list('🕛🕧🕐🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥🕚🕦'))

        try:
            while True:
                try:
                    self.pomodoro(int(input(mess)))
                except ValueError:
                    print("Wrong input. Try again.")
        except KeyboardInterrupt:
            print("\n Pomodoro's timer work has been interrupted.")

    def reverse_timer(self, sec: int) -> None:
        """
        - Clear up string and hide console cursor
        - Countdown
        - Clear string and show console cursor
        """
        self.write_flush(f"\x1b[A{55*' '}\r\x1b[?25l")
        for i in range(sec, 0, -1):
            self.write_flush(f'\r {self.animated_clock()}{self.lead_time(i)} ')
            time.sleep(1)
        self.write_flush(f"\r{35*' '}\r\x1b[?25h")

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

    @staticmethod
    def create_and_kill_background_process() -> None:
        """
        In order to hide the output of debugging information of the audio
        player, we will transfer the playback/generation code of the audio
        to a separate file and we will call this script in the background.
        Why so? - because standard output redirection does not work due to
        the specifics of ffmpeg it self.

        The process itself is needed to play the WAV file or the generated
        sound.
        """
        try:
            sound_py = os.path.abspath(os.path.dirname(__file__)) + '/sound.py'
            if not os.path.exists(sound_py):
                raise FileExistsError

            pid = subprocess.Popen(
                [sys.executable, sound_py],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            ).pid

            os.kill(pid, 0)
        except FileExistsError:
            print('File sound.py not fund')
        except ProcessLookupError:
            print('No such process')
        except PermissionError:
            print('Operation not permitted (i.e., process exists)')

    def pomodoro(self, minutes: int) -> None:
        """Run pomodoro"""
        self.reverse_timer(minutes * 60)
        self.create_and_kill_background_process()

        # Push-notifications on Linux desktop
        title = '⏰ Pomodoro: '
        info = f"{minutes} min TIME'S UP!"
        if sys.platform in ('linux', 'osx'):
            subprocess.call(['notify-send', title, info])
