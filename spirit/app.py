# -*- coding: utf-8 -*-
import tornado.web

from .routers import routers


class Application(tornado.web.Application):
    def __init__(self, config):
        settings = dict(
            autoescape=None,
            debug=config.DEBUG,
            cookie_secret=config.cookie_secret,
            template_path=config.template_path,
            static_path=config.static_path,
            xsrf_cookies=True,
        )

        tornado.web.Application.__init__(self, routers, **settings)
