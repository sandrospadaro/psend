# psend
Simple python utility for send push notifications.

## Description
A python client to send push notifications to phones and other device.

The notifications will recived by the "[Simple Push Notification API](https://play.google.com/store/apps/details?id=net.xdroid.pn)" App.

## How to install

You can install it using **pip**

```bash
pip install psend
```
## How to use

After installing this, it can be used by calling the script:

```bash
psend
```

or using python:

```bash
python -m psend
```

To use in your code:

```python
import psend

psend.psend(["My-Key"], "Title", "This is a payload", None)
```
## Options
The options for this utility can shown using `-h` flag:

```
usage: psend [-h] -k KEY [KEY ...] -t TITLE -c CONTENT [-u URL]

Utility to send push notification

options:
  -h, --help            show this help message and exit
  -k KEY [KEY ...], --keys KEY [KEY ...]
  -t TITLE, --title TITLE
  -c CONTENT, --content CONTENT
  -u URL, --url URL

Send push notification to Simple Push Notification API
(https://play.google.com/store/apps/details?id=net.xdroid.pn)
```

## How to build

This project is built using [poetry](https://python-poetry.org/):

```bash
poetry build
```

## References

* Git repository: https://github.com/sandrospadaro/psend
* Pypi repository: https://pypi.org/project/psend/