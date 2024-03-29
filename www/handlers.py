# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, time, json, logging, hashlib, base64, asyncio
from www.coroweb import get, post
from www.models import User, Comment, Blog, next_id
from www.config import configs

@get('/')
async def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time() - 120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time() - 3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time() - 7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }


# @get('/api/users')
# async def api_get_users():
#     users = await User.findAll(orderBy='created_at desc')
#     for u in users:
#         u.passwd = '******'
#     return dict(users=users)

@get('/register')
def register():
    return {
        '__template__': 'register.html'
    }

@post('/api/users')
def api_register_user(*, email, name, passwd):
    pass
