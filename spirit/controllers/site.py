# -*- coding: utf-8 -*-
# import tornado.web
from ._base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self):
        print self.application.db
        self.write('Index')
