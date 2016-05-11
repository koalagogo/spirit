# -*- coding: utf-8 -*-
from ._base import Config


class DevelopmentConfig(Config):
    def __init__(self):
        Config.__init__(self)
        self.xsrf_cookies = False


config = DevelopmentConfig()
