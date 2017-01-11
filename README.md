# SleekWebBot

SleekWebBot is an internet robot that visits a website and clicks on a specified web element.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine ready for development and testing purposes. 

### Prerequisites

* Python 2.7 Minimum
* Selenium 3.0.2
* Website to visit

### Installing

Clone sleek-web-bot to your machine

```
git clone https://github.com/kevinbazira/sleek-web-bot.git
```

## Usage

### Example of usage:

Run SleekWebBot in python

```
python SleekWebBot.py
```

If you have all the python - selenium environment prerequisites set, SleekWebBot will run and ask you a couple of questions which you should answer to enable the bot execute successfully as shown in the screenshot below.

![Snapshot of SleekWebBot in action](https://github.com/kevinbazira/sleek-web-bot/blob/master/SleekWebBot_Snapshot.jpg "SleekWebBot Snapshot")

Majorly what this program does is;

```
Ask you for specific inputs --> Opens Browser --> Loads specified URL --> Waits for specified time (x)  --> Finds specified element --> Clicks element  --> Waits for specified time (y) --> Closes Broswer  --> Repeats process for specified number of times (z)
```

This program also logs small messages at each key step when it is running.

### Modify SleekWebBot

Feel free to enhance SleekWebBot to suit your needs by editing the SleekWebBot.py file. It is heavily commented for you to easily find your way.

## Warning!

The End-User assumes sole responsibility for anything resulting from the use or modification to this program.

## Built With

* [Python](https://www.python.org/) - Programming Language
* [Selenium](http://www.seleniumhq.org/) - Browser Automation

## Contributing

Please read [CONTRIBUTING.md](https://github.com/kevinbazira/sleek-web-bot/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* @dakotasmith Talk on [How Python and Selenium can take your browser anywhere] (https://www.youtube.com/watch?v=l15ZJAbxCL8)
