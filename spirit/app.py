# -*- coding: utf-8 -*-
import tornado.web
import pymongo

from .routers import routers


class Application(tornado.web.Application):
    def __init__(self, config):
        settings = dict(
            autoescape=None,
            debug=config.DEBUG,
            cookie_secret=config.cookie_secret,
            template_path=config.template_path,
            static_path=config.static_path,
            xsrf_cookies=config.xsrf_cookies,
        )

        self.db = getattr(
            pymongo.MongoClient(config.mongodb_host, config.mongodb_port),
            config.db_name)

        tornado.web.Application.__init__(self, routers, **settings)
