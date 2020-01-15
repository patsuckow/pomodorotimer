import os
import datetime
import calendar
import webbrowser
import numpy as np
import matplotlib.pyplot as plt


class PeriodPomodoros:
    def __init__(self, dates: list, work: list, relaxation: list,
                 name_svg: str) -> None:
        # the width of the bars adn size figure img
        if len(work) > 2:
            width = 0.4
            fig_size = (9.2, 7)
        else:
            width = 0.2
            fig_size = (7, 6)

        name_periods = []
        for i in dates:
            year, month, day = i.split('-')
            date = datetime.datetime(int(year), int(month), int(day)).weekday()
            name_periods.append(calendar.day_name[date] + '\n')

        if len(work) > 21:
            days = dates
        else:
            days = [k + j for k, j in zip(name_periods, dates)]

        x = np.arange(len(days))  # the label locations
        fig, ax = plt.subplots(figsize=fig_size)
        rects_work = ax.bar(x - width / 2, work, width, label='work')
        rects_relaxation = ax.bar(x + width / 2, relaxation, width,
                                  label='relaxation')
        ax.set_title(f'Statistics Pomodoro`s for the last {len(work)} days:')
        ax.set_xticks(x)
        ax.set_xticklabels(days)
        ax.legend(bbox_to_anchor=(0.56, -0.2))
        ax.set_ylabel('Minutes')

        if len(work) > 7:
            for label in ax.xaxis.get_ticklabels():
                label.set_rotation(45 if len(work) <= 14 else 90)

        self.auto_label(rects_work, ax)
        self.auto_label(rects_relaxation, ax)
        fig.tight_layout()
        plt.savefig(name_svg, bbox_inches='tight')

    @staticmethod
    def auto_label(rects: list, ax) -> None:
        """
        Attach a text label above each bar in *rects*, displaying its height.
        """
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')


class CountPomodorosTime:
    def __init__(self, work: list, relaxation: list, name_svg: str) -> None:
        work = sum(work)
        relaxation = sum(relaxation)

        ax = plt.subplots(
            figsize=(9.2, 4.5),
            subplot_kw=dict(aspect="equal")
        )[1]

        wedges = ax.pie(
            [work, relaxation],
            autopct=lambda pct: self.calc_pct(pct, [work, relaxation + 1]),
            textprops=dict(color="w")
        )[0]

        ax.legend(
            wedges,
            [
                'work: {:.2f} hours'.format(work/60),
                'relaxation: {:.2f} hours'.format(relaxation/60)
            ],
            title="Count Pomodoro`s time:\n",
            loc="center left",
            bbox_to_anchor=(0.92, 0, 0.5, 1)
        )

        plt.savefig(name_svg, bbox_inches='tight')

    @staticmethod
    def calc_pct(pct: int, values: list) -> str:
        return "{} min\n{:.2f}%".format(int(pct/100 * np.sum(values)), pct)


def graph(dates: list, work: list, relaxation: list) -> None:
    path = os.path.dirname(__file__) + '/'

    # If there are old statistics image files, then delete them
    svg_1 = path + 'stat-1.svg'
    if os.path.exists(svg_1):
        os.remove(svg_1)
    svg_2 = path + 'stat-2.svg'
    if os.path.exists(svg_2):
        os.remove(svg_2)

    # If statistics for the requested period exists in the database, then
    # display it
    if work:
        if 1 < len(work) <= 31:
            PeriodPomodoros(dates=dates, work=work, relaxation=relaxation,
                            name_svg=path+'stat-1.svg')

        CountPomodorosTime(work=work, relaxation=relaxation,
                           name_svg=path+'stat-2.svg')

    webbrowser.open('file://' + path + 'stats.html')
