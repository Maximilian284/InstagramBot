# Instagram Bot
### A simple tool that automates your interactions with Instagram
## Installation:
#### **This bot runs only on Windows.**
#### Install the requirement with
```elm
pip install -r requirements.txt
```
#### Next place in a folder named 'drivers' the chromedriver of your current Chrome version. You can download chromedrivers on https://chromedriver.chromium.org/downloads. The folders sholud be:
```elm
>>> tree
C:.
├───drivers
│   └───chromediver_{driver_version}.exe
└───Instagram
    └───InstaBot.py
```
#### Replace {driver_version} with your current Chrome version. Next open 'InstaBot.py' with your editor and change line 10 with your driver folder.  
## Usage:
#### Run this to start
```elm
python -i InstaBot.py
```
#### - Write **bot.openInstagram()** for start.
#### - Command syntax is: **bot.*commad*(*args*)**.
#### - For help, write **help()**.