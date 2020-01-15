import os
import sys
import time
import argparse
import subprocess
from collections import deque
from .graph_statistic import graph
from .statistics_db import today_entry, read_all_entry, read_today_entry, \
                           delete_today_entry, delete_all_entry, close_db

try:
    assert sys.version_info >= (3, 6)
except Exception:
    raise SystemExit('Pomodoro Timer works with Python 3.6 or higher.')


class PomodoroTimer:
    """
    Created by Alexey Patsukov (patsuckow@yandex.ru) 🇷🇺
    CLI Pomodoro Timer - https://github.com/patsuckow/pomodorotimer
    """
    # String for bar pomodoro counting
    min_str = '|'
    # Clear up string
    UP_CLEAR_STR = f"\x1b[A{79*' '}\r"

    def __init__(self) -> None:
        # First, check if the argument was passed to get/remove statistics
        argument = self.arg()
        if argument in ['today', 'all', 'delete-today', 'delete-all']:
            if argument == 'today':
                dates, work, relaxation = read_today_entry()
                graph(dates, work, relaxation)
            elif argument == 'all':
                dates, work, relaxation = read_all_entry()
                graph(dates, work, relaxation)
            elif argument == 'delete-today':
                delete_today_entry()
            elif argument == 'delete-all':
                delete_all_entry()
            close_db()
            exit(0)
        else:
            # Clear console before setup Pomodoro timer
            if sys.platform in ('linux', 'osx'):
                subprocess.call('clear', shell=True)
            elif sys.platform in ('nt', 'dos', 'ce'):
                subprocess.call('cls', shell=True)

            self.stack_watch = deque(list('🕛🕧🕐🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥🕚🕦'))
            mess = "Input min: 25/5/15/30 for your Pomodoro, or 0 for exit: "
            mess_two = "\nPomodoro's timer work has been interrupted."
            try:
                while True:
                    try:
                        self.min = int(input(mess))
                    except ValueError:
                        self.write_flush(PomodoroTimer.UP_CLEAR_STR)
                        continue
                    self.write_flush(PomodoroTimer.UP_CLEAR_STR)
                    if self.min in [5, 15, 25, 30]:
                        self.pomodoro()
                    elif self.min == 0:
                        self.write_flush(PomodoroTimer.UP_CLEAR_STR)
                        if PomodoroTimer.min_str != '|':
                            print(PomodoroTimer.min_str + '|' + mess_two)
                        exit(0)
            except KeyboardInterrupt:
                print(mess_two)

        self.show_console_cursor()

    @staticmethod
    def arg() -> str:
        """Get the value of the argument --statistic passed to the script"""
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '--statistic',
            type=str,
            default='',
            help="provide an string: 'today', 'all', 'delete-today', "
                 "'delete-all' (default: '')"
        )

        return parser.parse_args().statistic

    def bar_pomodoro(self) -> None:
        """
        We highlight the timer scale for pomodoro in different colors,
        depending on the set time.
        """
        if self.min == 5:
            PomodoroTimer.min_str += f"\x1b[42m\x1b[1m {self.min} \x1b[0m"
        if self.min == 15:
            PomodoroTimer.min_str += f"\x1b[42m\x1b[1m  {self.min}  \x1b[0m|"
        elif self.min == 25:
            PomodoroTimer.min_str += f"\x1b[41m\x1b[1m   {self.min}   \x1b[0m"
        elif self.min == 30:
            PomodoroTimer.min_str += f"\x1b[42m\x1b[1m    {self.min}    \x1b[0m|"
        self.write_flush(PomodoroTimer.UP_CLEAR_STR)
        print(PomodoroTimer.min_str)

    def reverse_timer(self) -> None:
        """Countdown"""
        self.write_flush("\n" + PomodoroTimer.UP_CLEAR_STR)
        for i in range(self.min * 60, 0, -1):
            self.write_flush(f'\r{self.animated_clock()}{self.lead_time(i)} ')
            time.sleep(1)
        self.write_flush(f"\r{35*' '}\r")

    @staticmethod
    def write_flush(string: str) -> None:
        sys.stdout.write(string)
        sys.stdout.flush()

    @staticmethod
    def hide_console_cursor() -> None:
        """Hide console cursor: '\x1b[?25l'
        https://en.wikipedia.org/wiki/ANSI_escape_code#CSI_codes
        ('\033' same as '\x1b')
        """
        sys.stdout.write('\x1b[?25l')

    @staticmethod
    def show_console_cursor() -> None:
        """Show console cursor: '\x1b[?25h' """
        sys.stdout.write('\x1b[?25h')

    def lead_time(self, sec: int) -> str:
        """Elapsed Time Calculation"""
        minutes = int(sec // 60)
        seconds = round(sec % 60, 3)
        if seconds // 10 == 0:
            seconds = '0' + str(seconds)
        if self.min == 25:
            return f" Pomodoro timer: \x1b[31m\x1b[1m{minutes}:{seconds}\x1b[0m"
        elif self.min in [5, 15, 30]:
            return f" Pomodoro timer: \x1b[32m\x1b[1m{minutes}:{seconds}\x1b[0m"

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
            sound_py = os.path.dirname(__file__) + '/sound.py'
            if not os.path.exists(sound_py):
                raise FileExistsError

            pid = subprocess.Popen(
                [sys.executable, sound_py],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            ).pid

            os.kill(pid, 0)
        except FileExistsError:
            print('File sound.py not fund\n')
        except ProcessLookupError:
            print('No such process\n')
        except PermissionError:
            print('Operation not permitted (i.e., process exists)\n')

    def logging_statistics(self) -> None:
        """INSERT / UPDATE log statistic in DB

        According to the principle of the Pomodoro technique - if you are
        distracted while doing work, then you must interrupt the current time
        and start a new Pomodoro. And this means that you need to write time
        in to the database only after the specified time has passed and not
        earlier.

        If you follow this principle, the Pomodoro Technique will be for you
        exactly the tool for which it was invented, namely, not to calculate
        the time of your work and breaks in work, but to make you concentrate
        on continuous and concentrated execution of works during one Pomodoro,
        i.e. within 25 minutes.
        """
        work = 0
        relaxation = 0
        if self.min in [5, 15, 30]:
            relaxation = self.min
        else:
            work = self.min
        today_entry(work, relaxation)

    def pomodoro(self) -> None:
        """Run pomodoro"""
        self.hide_console_cursor()
        self.reverse_timer()
        self.create_and_kill_background_process()
        self.bar_pomodoro()
        self.logging_statistics()

        # Push-notifications on Linux desktop
        title = '⏰ Pomodoro: '
        info = f"{self.min} min TIME'S UP!"
        if sys.platform in ('linux', 'osx'):
            subprocess.call(['notify-send', title, info])

        if self.min in [15, 30]:
            time.sleep(4)
            print('One Pomodoro cycle is over.\n')
            self.show_console_cursor()
            exit(0)
