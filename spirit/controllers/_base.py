# -*- coding: utf-8 -*-
import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def prepare(self):
        pass

    def on_finish(self):
        pass
