#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开发环境配置
'''
Default configrations.
'''

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}