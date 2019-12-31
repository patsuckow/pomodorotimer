# pomodorotimer
Console Pomodoro timer with playing the melody of the signal or with the 
generation of an end time signal. Displays a push notification on Linux and 
Mac OS X.

Pomodoro Technique - [see](https://en.wikipedia.org/wiki/Pomodoro_Technique)

We call the program from any directory in the console and set the countdown 
time:

![Peek 2019-12-31 15-09](https://user-images.githubusercontent.com/12321741/71621330-bf92ed00-2bdf-11ea-9de7-823fd4f8e97e.gif)

When the time ends, a sound signal will be played, push notification will be 
displayed and it is proposed to enter a new countdown time:

![Peek 2019-12-31 15-12](https://user-images.githubusercontent.com/12321741/71621378-0ed91d80-2be0-11ea-8142-5a169b1fe408.gif)

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
pomodorotimer
```

or 

```
pomodoro
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
