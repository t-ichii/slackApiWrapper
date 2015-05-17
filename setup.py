#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name          = 'slackApiWrapper'
    ,version      = '0.1.1'
    ,description  = 'This is Wrapper of Slack APIs.'
    ,license      = 'MIT'
    ,author       = 'Takeru Ichii'
    ,author_email = 'takeru.ichii@facebook.com'
    ,url          = 'https://github.com/t-ichii/slackApiWrapper'
    ,py_modules   = ['slackApiWrapper']
    ,package_dir  = {'' : 'slackApiWrapper'}
    ,entry_points = {
        "console_scripts": [
            "slackApiWrapper=slackApiWrapper:main"
        ]
    }
)
