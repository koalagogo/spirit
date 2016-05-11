# -*- coding: utf-8 -*-
from .controllers import site, wechat


routers = [
    (r"/", site.IndexHandler),
    (r"/wx_interface", wechat.InterfaceHandler)
]
