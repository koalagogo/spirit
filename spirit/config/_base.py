# -*- coding: utf-8 -*-
import base64
import os
import uuid


def load_config(mode):
    if mode == 'development':
        from .development import config
    elif mode == 'production':
        from .production import config
    elif mode == 'testing':
        from .testing import config
    return config


class Config(object):
    def __init__(self):
        self.DEBUG = True
        self.xsrf_cookies = True
        self.cookie_secret = base64.b64encode(
            uuid.uuid4().bytes + uuid.uuid4().bytes)
        self.template_path = os.path.abspath('../templates/')
        self.static_path = os.path.abspath('../static')
        self.mongodb_host = '127.0.0.1'
        self.mongodb_port = 27017
        self.db_name = 'spirit'
