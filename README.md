# pomodorotimer (CLI Pomodoro Timer)
Console Pomodoro timer with playing the melody of the signal or with the 
generation of an end time signal. Displays a push notification on Linux and 
Mac OS X.

----
# Pomodoro Technique:
Pomodoro Technique - [see](https://en.wikipedia.org/wiki/Pomodoro_Technique)

![plan](https://user-images.githubusercontent.com/12321741/72369481-459b5180-3711-11ea-9bb6-e6eed7a4a1e4.jpg)

We will use the traditional Pomodoro scheme:

![technique](https://user-images.githubusercontent.com/12321741/72372975-77fc7d00-3718-11ea-944b-69e426dc30b2.png)

### It is important:
**According to the principle of the Pomodoro technique - if you are
distracted while doing work, then you must interrupt the current time
and start a new Pomodoro. And this means that you need to write time in to
the database only after the specified time has passed and not earlier.**

**If you follow this principle, the Pomodoro Technique will be for you exactly 
the tool for which it was invented, namely, not to calculate the time of your 
work and breaks in work, but to make you concentrate on continuous and 
concentrated execution of works during one Pomodoro, i.e. within 25 minutes.**

---

We call the program from any directory in the console and set the countdown 
time:

![1](https://user-images.githubusercontent.com/12321741/72445421-bcdcee00-37c2-11ea-863f-9f3fc9c36a9f.gif)

When the time ends, a sound signal will be played, push notification will be 
displayed and it is proposed to enter a new countdown time. And also, it will 
display the time that is OUT, in the form of a colored time bar, where:
- red color - working time (25 minutes)
- green color - time for a short or long break (5, 15 or 30 minutes)

![2](https://user-images.githubusercontent.com/12321741/72445482-cfefbe00-37c2-11ea-9a0f-6fe319b13946.gif)

![3](https://user-images.githubusercontent.com/12321741/72445528-e433bb00-37c2-11ea-82bb-44fb220ba732.gif)

![4 2](https://user-images.githubusercontent.com/12321741/72445885-82278580-37c3-11ea-9edc-fc5dedd40276.gif)

![5 2](https://user-images.githubusercontent.com/12321741/72446142-0a0d8f80-37c4-11ea-94bf-fc789bfb426b.gif)

The type of push notification depends on your OS and the type of graphical 
shell used, for example:

![Peek 2019-12-30 22-35](https://user-images.githubusercontent.com/12321741/71597566-cde7f700-2b54-11ea-83a9-133cc737d32c.gif)

## How to install:

#### From PyPI:

    pip3 install pomodorotimer --user

#### From sources:

Alternatively you can install **pomodorotimer** from sources directory:

    git clone https://github.com/patsuckow/pomodorotimer
    cd pomodorotimer
    pip3 install -r requirements.txt
    pip3 install . --user
    cd ..
    rm -rf pomodorotimer

## How run **pomodorotimer**:
```
pomodoro
```

## Work with statistics Pomodoro`s:

Get statistics today:
```
pomodoro --statistic=today
```
We get something like this in the browser window:

![stat-2](https://user-images.githubusercontent.com/12321741/72270776-b9b4f700-3636-11ea-972b-e92d767beaad.jpg)

All-Time Statistics:
```
pomodoro --statistic=all
```
We get something like this in the browser window:
![all](https://user-images.githubusercontent.com/12321741/72447777-f879b700-37c6-11ea-9fda-edd623b8442f.png)

Delete (clear) statistics for today:
```
pomodoro --statistic=delete-today
```
Delete (clear) all statistics:
```
pomodoro --statistic=delete-all
```

## Requirements:
See in requirements.txt

**pomodorotimer** works with ![version](https://user-images.githubusercontent.com/12321741/68495259-e298c480-0260-11ea-9d83-beab9b416562.png) or higher.


## Licence:
![GNU GPL v 3 0](https://user-images.githubusercontent.com/12321741/67310082-c4636280-f505-11e9-83a7-d23e8037c54f.png)

## Authors:

**Alexey Patsukov 🇷🇺** - [GitHub profile](https://github.com/patsuckow)

## Contributing:

### Submit issues

If you spotted something weird in application behavior or want to propose a 
feature you are welcome.

### Write code

If you are eager to participate in application development and to work on an 
existing issue (whether it should
be a bugfix or a feature implementation), fork, write code, and make a pull 
request right from the forked project page.

### Spread the word

If you have some tips and tricks or any other words that you think might be of 
interest for the others — publish it
wherever you find convenient.

### Help in the development of the project
If you want to help in the development of the project or just to thank the 
author, this can be done through PayPal: https://www.paypal.me/patsuckow

Read also:
- https://francescocirillo.com
- https://habr.com/ru/post/446996/
- http://career-philol.ru/page/adaptive/id341091/blog/3189767/
