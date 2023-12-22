from pathlib import Path
from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


def find_requires():
    requirements = []
    dir_path = Path(__file__).resolve().parent
    with open(dir_path / "requirements.txt") as f:
        requirements = f.readlines()

    return requirements


if __name__ == "__main__":
    ver = "0.2.5"

    setup(
        name="pomodorotimer",
        version=ver,
        url="https://github.com/patsuckow/pomodorotimer",
        project_urls={
            "Bug Tracker": "https://github.com/patsuckow/pomodorotimer/issues",
            "Donate": "https://www.paypal.me/patsuckow",
        },
        description="CLI Pomodoro Timer",
        long_description=long_description,
        long_description_content_type="text/markdown",
        license="GNU General Public License v3 (GPLv3)",
        author="Alexey Patsukov 🇷🇺",
        author_email="patsuckow@yandex.ru",
        python_requires=">=3.10.13",
        keywords=[
            "pomodoro",
            "tomato",
            "pomodorotimer",
            "pomodoro timer",
            "pomodoro technique",
            "productivity",
            "time management",
            "countdown",
            "stopwatch",
            "timer",
            "eta",
            "freelance",
            "freelancing",
            "CLI",
        ],
        classifiers=[
            # As in https://pypi.python.org/pypi?:action=list_classifiers
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Intended Audience :: Developers",
            "Topic :: Utilities",
        ],
        # Specify an executable console file
        entry_points={
            "console_scripts": [
                "pomodoro = pomodorotimer.pomodorotimer:PomodoroTimer",
            ],
        },
        include_package_data=True,
        packages=find_packages(
            exclude=[
                # '*.tests', '*.tests.*', 'tests',
                # '*.img', '*.img.*', 'img',
                # '*..github', '*..github.*', '.github'
            ]
        ),
        zip_safe=False,  # the package can run out of an .egg file
        install_requires=find_requires(),
        setup_requires=[],
        # test_suite='tests',
        # tests_require=[],
    )