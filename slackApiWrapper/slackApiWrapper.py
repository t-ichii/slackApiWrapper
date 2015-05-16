#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Takeru Ichii'

import requests
import json
import argparse

class slackApiWrapper:
	def __init__(self, token):
		self.token = token
		self.url   = 'https://slack.com/api/'
	def send(self, api_name, arg = {}):
		api_url = self.url + api_name
		header = {'token' : self.token}
		try:
			header.update(arg)
		except:
			pass
		responce = requests.post(api_url ,params = header)
		return responce

def main():
	argument_parser = argparse.ArgumentParser(description='This is Wrapper of Slack APIs.')
	argument_parser.add_argument('-t', '--token', type=str, required=True , help='Check out https://api.slack.com/web')
	argument_parser.add_argument('-A', '--api'  , type=str, required=True , help='Check out https://api.slack.com/methods E.x) api.test')
	argument_parser.add_argument('-a', '--arg'  , type=str, required=False, help='E.x) {"foo" : "test_arg"}')
	args = vars(argument_parser.parse_args())
	slack_client = slackApiWrapper(args['token'])
	send_result = slack_client.send(args['api'], json.loads(args['arg']))
	return send_result.text

if __name__ == '__main__':
	print(main())
