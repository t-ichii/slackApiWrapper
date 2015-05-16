# slackApiWrapper

## Description

This is Wrapper of Slack APIs.

## Required module

* requests
* json

## Installation

clone this repo

```
$ git clone https://github.com/t-ichii/slackApiWrapper.git
```

execute setup.py

```
$ cd slackApiWrapper
$ python setup.py install
```

# Usage

### In Python

```
import slackApiWrapper

slack_token = 'xxxx-xxxxxxxxxx-xxxxxxxxxx-xxxxxxxxxx-xxxxxx'
api_name = 'api.test'
arg = {'foo' : 'test'}
slack_client = slackApiWrapper(slack_token)
send_result = slack_client.send(api_name, arg)
print(send_result.text)
```


### In Shell

```
$ slackApiWrapper -h
usage: slackApiWrapper [-h] -t TOKEN -A API [-a ARG]

This is Wrapper of Slack APIs.

optional arguments:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        Check out https://api.slack.com/web
  -A API, --api API     Check out https://api.slack.com/methods E.x) api.test
  -a ARG, --arg ARG     E.x) {"foo" : "test_arg"}
  
$ slackApiWrapper \
-t xxxx-xxxxxxxxxx-xxxxxxxxxx-xxxxxxxxxx-xxxxxx \
-A api.test \
-a '{"foo" : "test"}'
{"ok":true,"args":{"token":"xxxx-xxxxxxxxxx-xxxxxxxxxx-xxxxxxxxxx-xxxxxx","foo":"test"}}
```